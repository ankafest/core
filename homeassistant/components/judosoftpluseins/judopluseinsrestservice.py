"""Restobject. A REST object define: connect/disconnect, attach, get Numbers and put Switch "stop/start"."""

from datetime import datetime
from functools import partial
import logging

import requests

from homeassistant.config_entries import ConfigEntry
from homeassistant.const import (
    ATTR_NAME,
    CONF_DEVICE,
    CONF_PASSWORD,
    CONF_PORT,
    CONF_USERNAME,
    URL_API,
)
from homeassistant.core import HomeAssistant

from . import const
from .myexceptions import GetRequestException

log = logging.getLogger(__name__)


class JudoRestAPI:
    """RestApi for To JudoAPI."""

    def __init__(self, hass: HomeAssistant) -> None:
        """Initializing the input data."""
        self.homeassisant = hass
        self.passwort = ConfigEntry.data[CONF_PASSWORD]
        self.username = ConfigEntry.data[CONF_USERNAME]
        self.serial_nummber = ConfigEntry.data[const.SERIAL_NUMBER]
        self.base_url = (
            "https://"
            + str(ConfigEntry.data[URL_API])
            + ":"
            + str(ConfigEntry.data[CONF_PORT])
        )
        self.connected = False
        self.standby_status = None
        self.login_param = {
            const.GROUP: const.GROUP_REGISTER,
            const.COMMAND: const.COMMAND_LOGIN,
            ATTR_NAME: const.COMMAND_LOGIN,
            CONF_USERNAME: self.username,
            CONF_PASSWORD: self.passwort,
            const.ROLE: const.ROLE_CUSTOMER,
        }
        self.connect_param = {
            const.GROUP: const.GROUP_REGISTER,
            const.COMMAND: const.COMMAND_CONNECT,
            const.SERIAL_NUMBER: self.serial_nummber,
            CONF_DEVICE: const.DEFAULT_DEVICE,
        }
        self.consumption_request = {
            const.GROUP: const.GROUP_CONSUMPTION,
        }
        self.waterstop_request = {
            const.GROUP: const.GROUP_WATERSTOP,
            const.COMMAND: str(const.COMMAND_STANDBY),
        }
        self.error_message_response_status = (
            "RequestException after %1 response_status = %2 "
        )
        self.error_during_get_request = "An error raised during get-request for %1"
        self.token = self.async_login_and_connect()

    async def get_request(self, params, topic):
        """Get-Request for all judo-requests."""
        params = params | {const.TOKEN: self.token}
        try:
            response = await self.homeassisant.async_add_executor_job(
                partial(requests.get, url=self.base_url, params=params, timeout=30)
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
        return response.json()[const.DATA]

    async def async_login_and_connect(self):
        """Connect to Judo Api."""
        response = await self.get_request(
            params=self.login_param, topic=const.COMMAND_LOGIN
        )

        json_response = response.json()
        token = str(json_response["token"])
        await self.get_request(params=self.connect_param, topic=const.COMMAND_CONNECT)
        return token

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
            const.COMMAND: (
                const.COMMAND_WATER_DAILY
                if day is not None
                else const.COMMAND_WATER_WEEKLY
                if week_of_day is not None
                else const.COMMAND_WATER_MONTHLY
                if month is not None and day is None and week_of_day is None
                else const.COMMAND_WATER_YEARLY
            )
        }

    def get_water_consumptiom_request_param(
        self, year, month=None, day=None, week_of_day=None
    ):
        """Get time-parameter for consumption-request."""
        params = {const.YEAR: year}
        if month is not None:
            params[const.MONTH] = month
        if day is not None:
            params[const.DAY] = day
        if week_of_day is not None:
            params[const.DAYS] = week_of_day
        if day is not None:
            params[const.DAY] = day
        return params

    async def async_get_salt_consumption_request(self, command):
        """Request of type Consumptions."""
        params = self.consumption_request | {const.COMMAND: command}
        return await self.get_request(params=params, topic="salt-consumption")

    async def async_set_waterstop(self, on_off=const.COMMAND_WATERSTOP_START):
        """Request of type Consumptions."""
        params = self.waterstop_request
        response = await self.get_request(params=params, topic=const.GROUP_WATERSTOP)
        device_status = response.json()[const.DATA]
        if (device_status == "0" and on_off == const.COMMAND_WATERSTOP_STOP) or (
            device_status != "0" and on_off == const.COMMAND_WATERSTOP_START
        ):
            params = self.waterstop_request | {const.PARAMETER: on_off}
            await self.get_request(
                params=params, topic=const.GROUP_WATERSTOP + " set " + on_off
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
            const.GROUP: const.GROUP_REGISTER,
            const.COMMAND: const.COMMAD_LOGOUT,
            const.TOKEN: self.token,
        }
        await self.get_request(params=params, topic=const.COMMAD_LOGOUT)
        self.token = None
