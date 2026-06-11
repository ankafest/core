"""The Judo Soft Plus Eins integration."""

from __future__ import annotations

from homeassistant.config_entries import ConfigEntry
from homeassistant.const import Platform
from homeassistant.core import HomeAssistant

from .configentry import MyConfigEntry, MyData
from .const import REST_ITEMS
from .coordinator import MyCoordinator
from .judoisoftplusrestservice import JudoRestAPI

# For your initial PR, limit it to 1 platform.
_PLATFORMS: list[Platform] = [
    Platform.BUTTON,
    Platform.NUMBER,
    Platform.SENSOR,
]


async def async_setup_entry(hass: HomeAssistant, entry: MyConfigEntry) -> bool:
    """Set up Judo Soft Plus Eins from a config entry."""

    rest_api = JudoRestAPI(config_entry=entry, hass=hass)
    coordinator = MyCoordinator(
        hass=hass, my_api=rest_api, api_items=REST_ITEMS, config_entry=entry
    )
    await coordinator.async_config_entry_first_refresh()
    entry.runtime_data = MyData(
        rest_api=rest_api,
        coordinator=coordinator,
        hass=hass,
    )

    await hass.config_entries.async_forward_entry_setups(entry, _PLATFORMS)

    return True


async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Unload a config entry."""
    await entry.runtime_data.rest_api.async_logout()
    return await hass.config_entries.async_unload_platforms(entry, _PLATFORMS)
