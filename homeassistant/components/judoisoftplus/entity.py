"""Entities for projects."""

from homeassistant.components.sensor.const import SensorStateClass
from homeassistant.helpers.device_registry import DeviceInfo
from homeassistant.helpers.entity import Entity

from .configentry import MyConfigEntry
from .const import DEVICE, DOMAIN
from .item import EntityItem
from .judoisoftplusrestservice import JudoRestAPI


class MyEntity(Entity):
    """An entity using CoordinatorEntity.

    The CoordinatorEntity class provides:
    should_poll
    async_update
    async_added_to_hass
    available

    The base class for entities that hold general parameters
    """

    _attr_should_poll = True
    _attr_has_entity_name = True

    def __init__(
        self,
        config_entry: MyConfigEntry,
        entity_item: EntityItem,
        rest_api: JudoRestAPI,
    ) -> None:
        """Initialize the entity."""
        self._config_entry = config_entry
        self._entity_item = entity_item
        self._rest_api = rest_api

        dev_postfix = "_"

        if dev_postfix == "_":
            dev_postfix = ""

        self._dev_device = DEVICE

        self._attr_translation_key = self._entity_item.translation_key
        if self._entity_item.unit_of_measurement != " ":
            self._attr_state_class = SensorStateClass.MEASUREMENT
            self._attr_unit_of_measurement = self._entity_item.unit_of_measurement
            self._attr_native_unit_of_measurement = (
                self._entity_item.unit_of_measurement
            )

        self._attr_unique_id = (
            DOMAIN + "_" + self._dev_device + "_" + self._entity_item.translation_key
        )

        self._rest_api = rest_api
        self._attr_icon = self._entity_item.icon

    def my_device_info(self) -> DeviceInfo:
        """Build the device info."""
        return {
            "identifiers": {(DOMAIN, DEVICE)},
            "sw_version": "Device_SW_Version",
            "model": "Device_model",
            "manufacturer": "Judo",
            "name": DEVICE,
        }

    @property
    def device_info(self) -> DeviceInfo:
        """Return device info."""
        return MyEntity.my_device_info(self)
