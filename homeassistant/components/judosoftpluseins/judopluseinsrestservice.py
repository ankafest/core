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
    COMMAND,
    COMMAND_CONNECT,
    COMMAND_LOGIN,
    COMMAND_SALT_QUANTITY,
    COMMAND_SALT_RANGE,
    COMMAND_STANDBY,
    COMMAND_WATER_AVERAGE,
    COMMAND_WATER_CURRENT,
    COMMAND_WATER_TOTAL,
    DATA,
    DEFAULT_DEVICE,
    GROUP,
    GROUP_CONSUMPTION,
    GROUP_REGISTER,
    GROUP_WATERSTOP,
    PARAMETER,
    ROLE,
    ROLE_CUSTOMER,
    SERIAL_NUMBER,
    TOKEN,
    USER,
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
            COMMAND: COMMAND_STANDBY,
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
            response = await self.homeassisant.async_add_executor_job(
                partial(
                    requests.get,
                    url=self.base_url,
                    params=self.login_param,
                    timeout=60,
                    verify=False,
                )
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
        return True

    async def async_get_current_water_consumption(self):
        """Get current water consumption."""
        params = self.consumption_request | {COMMAND: COMMAND_WATER_CURRENT}
        data = await self.get_request(params, "current water consumption")
        return data

    async def async_get_total_water_consumption(self):
        """Get total water consumption."""
        params = self.consumption_request | {COMMAND: COMMAND_WATER_TOTAL}
        data = await self.get_request(params, "total water consumption")
        return data

    async def async_get_average_water_consumption(self):
        """Get average water consumption."""
        params = self.consumption_request | {COMMAND: COMMAND_WATER_AVERAGE}
        data = await self.get_request(params, "average water consumption")
        return data

    async def async_get_waterstop_standby(self):
        """Get waterstop to standby."""
        params = self.waterstop_request
        data = await self.get_request(params, "get waterstop to standby")
        return data

    async def async_get_salt_range(self):
        """Get salt range."""
        params = self.consumption_request | {COMMAND: COMMAND_SALT_RANGE}
        data = await self.get_request(params, "salt range")
        return data

    async def async_salt_quantity(self):
        """Get salt quantity."""
        params = self.consumption_request | {COMMAND: COMMAND_SALT_QUANTITY}
        data = await self.get_request(params, "salt quantity")
        return data
