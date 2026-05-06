"""Restobject. A REST object define: connect/disconnect, attach, get Numbers and put Switch "stop/start"."""

from datetime import datetime
from functools import partial
import logging

import requests

from homeassistant.config_entries import ConfigEntry
from homeassistant.const import (
    ATTR_NAME,
    CONF_PASSWORD,
    CONF_PORT,
    CONF_URL,
    CONF_USERNAME,
)
from homeassistant.core import HomeAssistant

from .const import (
    COMMAD_LOGOUT,
    COMMAND,
    COMMAND_CONNECT,
    COMMAND_LOGIN,
    COMMAND_STANDBY,
    COMMAND_WATER_DAILY,
    COMMAND_WATER_MONTHLY,
    COMMAND_WATER_WEEKLY,
    COMMAND_WATER_YEARLY,
    COMMAND_WATERSTOP_START,
    COMMAND_WATERSTOP_STOP,
    DATA,
    DAY,
    DAYS,
    DEFAULT_DEVICE,
    GROUP,
    GROUP_CONSUMPTION,
    GROUP_REGISTER,
    GROUP_WATERSTOP,
    MONTH,
    PARAMETER,
    ROLE,
    ROLE_CUSTOMER,
    SERIAL_NUMBER,
    TOKEN,
    USER,
    YEAR,
)
from .myexceptions import GetRequestException

log = logging.getLogger(__name__)


class JudoRestAPI:
    """RestApi for To JudoAPI."""

    def __init__(self, config_entry: ConfigEntry, hass: HomeAssistant) -> None:
        """Initializing the input data."""
        self.homeassisant = hass
        self.passwort = config_entry.data[CONF_PASSWORD]
        self.username = config_entry.data[CONF_USERNAME]
        self.serial_nummber = config_entry.data[SERIAL_NUMBER]
        self.base_url = (
            "https://"
            + str(config_entry.data[CONF_URL])
            + ":"
            + str(config_entry.data[CONF_PORT])
            + "/"
        )
        self.connected = False
        self.standby_status = None
        self.login_param = {
            GROUP: GROUP_REGISTER,
            COMMAND: COMMAND_LOGIN,
            ATTR_NAME: COMMAND_LOGIN,
            USER: self.username,
            CONF_PASSWORD: self.passwort,
            ROLE: ROLE_CUSTOMER,
        }
        self.connect_param = {
            GROUP: GROUP_REGISTER,
            COMMAND: COMMAND_CONNECT,
            SERIAL_NUMBER: self.serial_nummber,
            PARAMETER: DEFAULT_DEVICE,
        }
        self.consumption_request = {
            GROUP: GROUP_CONSUMPTION,
        }
        self.waterstop_request = {
            GROUP: GROUP_WATERSTOP,
            COMMAND: str(COMMAND_STANDBY),
        }
        self.error_message_response_status = (
            "RequestException after %1 response_status = %2 "
        )
        self.error_during_get_request = "An error raised during get-request for %1"
        self.token = None
        if self.async_login_and_connect():
            log.info("Successfully logged in and connected to Judo API")
        else:
            log.error("Failed to log in and connect to Judo API")

    async def get_request(self, params, topic):
        """Get-Request for all judo-requests."""
        params = params | {TOKEN: self.token}
        try:
            response = await self.homeassisant.async_add_executor_job(
                partial(
                    requests.get,
                    url=self.base_url,
                    params=params,
                    timeout=60,
                    verify=False,
                )
            )
            if response.status_code != 200:
                log.error(
                    self.error_message_response_status,
                    topic,
                    response.status_code,
                )
                raise requests.exceptions.RequestException
        except GetRequestException:
            log.info(self.error_during_get_request, "waterstop")
        return response.json()[DATA]

    async def async_login_and_connect(self):
        """Connect to Judo Api."""
        try:
            myurl = (
                self.base_url
                + "?group="
                + GROUP_REGISTER
                + "&command="
                + COMMAND_LOGIN
                + "&name="
                + COMMAND_LOGIN
                + "&user="
                + self.username
                + "&password="
                + self.passwort.replace("#", "%23")
                + "&role="
                + ROLE_CUSTOMER
            )
            response = await self.homeassisant.async_add_executor_job(
                partial(requests.get, url=myurl, timeout=60, verify=False)
            )
            if response.status_code != 200:
                log.error(
                    self.error_message_response_status,
                    "Login",
                    response.status_code,
                )
                raise requests.exceptions.RequestException
        except GetRequestException:
            log.info(self.error_during_get_request, "Login")
        json_response = response.json()

        a = response.json()
        __token = str(json_response["token"])
        params = self.connect_param | {TOKEN: __token}
        try:
            response = await self.homeassisant.async_add_executor_job(
                partial(
                    requests.get,
                    url=self.base_url,
                    params=params,
                    timeout=60,
                    verify=False,
                )
            )
            if response.status_code != 200:
                log.error(
                    self.error_message_response_status,
                    "Connect",
                    response.status_code,
                )
                raise requests.exceptions.RequestException
        except GetRequestException:
            log.info(self.error_during_get_request, "Connect")
        self.token = __token
        a = response.json()
        return True

    async def async_get_water_consumption_request(
        self, year, month=None, week_of_day=None, day=None
    ):
        """Request of type Consumptions."""
        command = self.get_water_consumption_request_command(
            year, month, week_of_day, day
        )
        time_params = self.get_water_consumptiom_request_param(
            year=year, month=month, day=day, week_of_day=week_of_day
        )
        params = self.consumption_request | command | time_params
        return await self.get_request(params=params, topic="water-consumption")

    def get_water_consumption_request_command(
        self, year, month=None, week_of_day=None, day=None
    ):
        """Get 'command='+ command for consumption request."""
        return {
            COMMAND: (
                COMMAND_WATER_DAILY
                if day is not None
                else COMMAND_WATER_WEEKLY
                if week_of_day is not None
                else COMMAND_WATER_MONTHLY
                if month is not None and day is None and week_of_day is None
                else COMMAND_WATER_YEARLY
            )
        }

    def get_water_consumptiom_request_param(
        self, year, month=None, day=None, week_of_day=None
    ):
        """Get time-parameter for consumption-request."""
        params = {YEAR: year}
        if month is not None:
            params[MONTH] = month
        if day is not None:
            params[DAY] = day
        if week_of_day is not None:
            params[DAYS] = week_of_day
        if day is not None:
            params[DAY] = day
        return params

    async def async_get_salt_consumption_request(self, command):
        """Request of type Consumptions."""
        params = self.consumption_request | {COMMAND: command}
        return await self.get_request(params=params, topic="salt-consumption")

    async def async_set_waterstop(self, on_off=COMMAND_WATERSTOP_START):
        """Request of type Consumptions."""
        params = self.waterstop_request
        response = await self.get_request(params=params, topic=GROUP_WATERSTOP)
        device_status = response.json()[DATA]
        if (device_status == "0" and on_off == COMMAND_WATERSTOP_STOP) or (
            device_status != "0" and on_off == COMMAND_WATERSTOP_START
        ):
            params = self.waterstop_request | {PARAMETER: on_off}
            await self.get_request(
                params=params, topic=GROUP_WATERSTOP + " set " + on_off
            )

    async def async_get_water_consumtion_of_day(self):
        """Get water consumption of day."""
        return await self.async_get_water_consumption_request(
            year=datetime.now().year,
            month=datetime.now().month,
            day=datetime.now().day,
        )

    async def async_get_water_consumtion_of_week(self):
        """Get water consumption of week."""
        return await self.async_get_water_consumption_request(
            year=datetime.now().year,
            month=datetime.now().month,
            week_of_day=datetime.now(),
        )

    async def async_get_water_consumtion_of_month(self):
        """Get water consumption of month."""
        return await self.async_get_water_consumption_request(
            year=datetime.now().year, month=datetime.now().month
        )

    async def async_get_water_consumtion_of_year(self):
        """Get water consumption of year."""
        return await self.async_get_water_consumption_request(year=datetime.now().year)

    async def async_logout(self):
        """Logout of Judo API."""
        params = {
            GROUP: GROUP_REGISTER,
            COMMAND: COMMAD_LOGOUT,
            TOKEN: self.token,
        }
        await self.get_request(params=params, topic=COMMAD_LOGOUT)
        self.token = None
