"""my config entry."""

from dataclasses import dataclass
from typing import Any

from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant


@dataclass
class MyData:
    """My config data."""

    rest_api: Any
    hass: HomeAssistant
    coordinator: Any


type MyConfigEntry = ConfigEntry[MyData]
