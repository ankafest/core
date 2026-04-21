"""Config flow for the Judo Soft Plus Eins integration."""

from typing import Any

import voluptuous as vol

from homeassistant import config_entries, const, exceptions
import homeassistant.helpers.config_validation as cv

from .const import DOMAIN, SERIAL_NUMBER


class ConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    """Handle a config flow for Judo Soft Plus Eins."""

    VERSION = 2
    # Pick one of the available connection classes in homeassistant/config_entries.py
    # This tells HA if it should be asking for updates, or it'll be notified of updates
    # automatically. This example uses PUSH, as the dummy hub will notify HA of
    # changes.
    CONNECTION_CLASS = config_entries.CONN_CLASS_LOCAL_PUSH

    async def async_step_user(self, user_input=None) -> config_entries.ConfigFlowResult:
        """Step for setup process."""

        data_schema = vol.Schema(
            schema={
                vol.Required(schema=const.CONF_URL): cv.url,
                vol.Optional(schema=const.CONF_PORT, default="80"): cv.port,
                vol.Optional(schema=const.CONF_USERNAME, default="admin"): cv.string,
                vol.Optional(schema=const.CONF_PASSWORD): cv.string,
                vol.Required(schema=SERIAL_NUMBER): cv.string,
                vol.Optional(schema=const.CONF_SCAN_INTERVAL, default="60"): cv.string,
            }
        )

        errors = {}
        info = None
        if user_input is not None:
            try:
                info = await validate_input(data=user_input)

                return self.async_create_entry(title=info["title"], data=user_input)

            except Exception:  # noqa: BLE001
                errors["base"] = "unknown error"
        await self.async_set_unique_id(const.CONF_URL)
        self._abort_if_unique_id_configured()
        # If there is no user input or there were errors, show the form again,
        # #including any errors that were found with the input.
        return self.async_show_form(
            step_id="user",
            data_schema=data_schema,
            errors=errors,
            description_placeholders={
                const.CONF_URL: "url",
                const.CONF_PORT: "port",
                const.CONF_USERNAME: "username",
                const.CONF_PASSWORD: "password",
                SERIAL_NUMBER: "serial_number",
                const.CONF_SCAN_INTERVAL: "scan_interval",
            },
        )


async def validate_input(data: dict) -> dict[str, Any]:
    """Validate the input."""

    if len(data["host"]) < 3:
        raise InvalidHost

    return {"title": data["host"]}


class InvalidHost(exceptions.HomeAssistantError):
    """Error to indicate there is an invalid hostname."""
