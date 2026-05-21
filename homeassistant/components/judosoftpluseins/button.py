"""Button for Waterstop on/off."""

import logging

from homeassistant.components.button import ButtonEntity
from homeassistant.core import HomeAssistant
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback
from homeassistant.helpers.update_coordinator import CoordinatorEntity

from .configentry import MyConfigEntry
from .const import (
    BUTTON_ITEMS,
    COMMAND_REGENERATION,
    TRANSLATION_KEY_SET_STANDBY_OFF,
    TRANSLATION_KEY_SET_STANDBY_ON,
)
from .coordinator import MyCoordinator
from .entity import EntityItem, MyEntity

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
    for item in BUTTON_ITEMS:
        for entity in item.list_of_entites:
            mysensor = WaterstopButtonEntity(
                config_entry=config_entry,
                entity_item=entity,
                coordinator=coordinator,
                idx=index,
            )
            entries.append(mysensor)
            index += 1

    async_add_entities(
        entries,
        update_before_add=True,
    )


class WaterstopButtonEntity(CoordinatorEntity, ButtonEntity, MyEntity):
    """Representation of a button to start or stop the waterstop."""

    def __init__(
        self,
        config_entry: MyConfigEntry,
        entity_item: EntityItem,
        coordinator: MyCoordinator,
        idx: int,
    ) -> None:
        self._idx = idx
        self._entity_item = entity_item
        """Initialize the button."""
        self._rest_api = coordinator.rest_api
        super().__init__(coordinator=coordinator, context=idx)
        MyEntity.__init__(
            self,
            config_entry=config_entry,
            entity_item=entity_item,
            rest_api=self._rest_api,
        )

    async def async_press(self) -> None:
        """Turn the entity on."""
        if self._entity_item.translation_key == TRANSLATION_KEY_SET_STANDBY_OFF:
            await self._rest_api.async_set_waterstop_standby(on_off_command="start")
        elif self._entity_item.translation_key == TRANSLATION_KEY_SET_STANDBY_ON:
            await self._rest_api.async_set_waterstop_standby(on_off_command="stop")
        elif self._entity_item.translation_key == COMMAND_REGENERATION:
            await self.async_regerate()

    async def async_regerate(self) -> None:
        """Start the regeneration."""
        if await self._rest_api.async_get_is_judo_regenerate():
            logging.getLogger(__name__).info("Regeneration is already running.")
        else:
            await self._rest_api.async_set_regeneration()
