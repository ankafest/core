"""Number Entities  for judoisoftplus."""

import logging

from homeassistant.components.number import NumberEntity
from homeassistant.core import HomeAssistant, callback
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback
from homeassistant.helpers.update_coordinator import CoordinatorEntity

from .configentry import MyConfigEntry
from .const import NUMBER_TYPE, REST_ITEMS
from .coordinator import MyCoordinator
from .entity import MyEntity
from .item import EntityItem

logging.basicConfig()
log: logging.Logger = logging.getLogger(name=__name__)


async def async_setup_entry(
    hass: HomeAssistant,
    config_entry: MyConfigEntry,
    async_add_entities: AddConfigEntryEntitiesCallback,
) -> None:
    """Start with an empty list of entries."""
    entries = []

    coordinator = config_entry.runtime_data.coordinator
    index = 0
    for item in REST_ITEMS:
        if item.format == NUMBER_TYPE:
            for entity in item.list_of_entites:
                mynumber = MyNumberEntity(
                    config_entry=config_entry,
                    entity_item=entity,
                    coordinator=coordinator,
                    idx=index,
                )
                entries.append(mynumber)
                index += 1

    async_add_entities(
        entries,
        update_before_add=True,
    )


class MyNumberEntity(CoordinatorEntity, NumberEntity, MyEntity):
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
        coordinator: MyCoordinator,
        idx,
    ) -> None:
        """Initialize of MyNumberEntity."""
        super().__init__(coordinator, context=idx)
        self.idx = idx
        self._entity_item = entity_item
        self._rest_api = coordinator.rest_api
        MyEntity.__init__(self, config_entry, entity_item, coordinator.rest_api)

    @callback
    def _handle_coordinator_update(self) -> None:
        """Handle updated data from the coordinator."""
        self._attr_native_value = float(self._entity_item.result)
        self.async_write_ha_state()

    async def async_set_native_value(self, value: float) -> None:
        """Send value over modbus and refresh HA."""
        await self._rest_api.async_set_residual_waterhardness(value)
        self._attr_native_value = float(self._entity_item.result)
        self.async_write_ha_state()
