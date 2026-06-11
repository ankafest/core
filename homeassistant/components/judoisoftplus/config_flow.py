"""Config flow for the Judo Soft Plus Eins integration."""

from typing import Any

import voluptuous as vol

from homeassistant import config_entries, exceptions
from homeassistant.const import (
    CONF_PASSWORD,
    CONF_PORT,
    CONF_SCAN_INTERVAL,
    CONF_URL,
    CONF_USERNAME,
)
import homeassistant.helpers.config_validation as cv

from .const import DOMAIN, SERIAL_NUMBER, TITLE


class ConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    """Handle a config flow for Judo ISoft Plus."""

    VERSION = 2

    async def async_step_user(self, user_input=None) -> config_entries.ConfigFlowResult:
        """Step for setup process."""

        data_schema = vol.Schema(
            schema={
                vol.Required(
                    schema=CONF_URL, default="saturn.private.v4.mudal.net"
                ): cv.string,
                vol.Optional(schema=CONF_PORT, default="8124"): cv.port,
                vol.Optional(schema=CONF_USERNAME, default="uwefest"): cv.string,
                vol.Optional(schema=CONF_PASSWORD, default="dUjf%230124"): cv.string,
                vol.Required(schema=SERIAL_NUMBER, default="193960"): cv.string,
                vol.Optional(schema=CONF_SCAN_INTERVAL, default="60"): cv.string,
            }
        )

        errors = {}
        info = None
        if user_input is not None:
            try:
                info = await validate_input(data=user_input)
            except Exception:  # pylint: disable=broad-except
                errors["base"] = "unknown error"
            else:
                await self.async_set_unique_id(info[TITLE])
                self._abort_if_unique_id_configured()
                return self.async_create_entry(title=info[TITLE], data=user_input)
        # If there is no user input or there were errors, show the form again,
        # #including any errors that were found with the input.
        return self.async_show_form(
            step_id="user",
            data_schema=data_schema,
            errors=errors,
            description_placeholders={
                CONF_URL: "url",
                CONF_PORT: "port",
                CONF_USERNAME: "username",
                CONF_PASSWORD: "password",
                SERIAL_NUMBER: "serial_number",
                CONF_SCAN_INTERVAL: "scan_interval",
            },
        )


async def validate_input(data: dict) -> dict[str, Any]:
    """Validate the input."""
    if len(data[CONF_URL]) < 3:
        raise InvalidHost

    return {"title": data[CONF_URL]}


class InvalidHost(exceptions.HomeAssistantError):
    """Error to indicate there is an invalid hostname."""
