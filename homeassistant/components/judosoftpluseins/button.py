"""Button for Waterstop on/off."""

import logging

from homeassistant.components.button import ButtonEntity
from homeassistant.core import HomeAssistant
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback
from homeassistant.helpers.update_coordinator import CoordinatorEntity

from .configentry import MyConfigEntry
from .const import (
    BUTTON_ITEMS,
    CLOSE,
    COMMAND_REGENERATION,
    OPEN,
    START,
    STOP,
    TRANSLATION_KEY_SET_STANDBY_OFF,
    TRANSLATION_KEY_SET_STANDBY_ON,
    TRANSLATION_KEY_OF_GARTEN_IRRIGATION,
    TRANSLATION_KEY_OF_NORMAL_WATEROPERATION,
    TRANSLATION_KEY_OF_POOL_FILL_UP,
    TRANSLATION_KEY_OF_REFILL_BOILER_HEATING,
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
            mybutton = MyButtonEntity(
                config_entry=config_entry,
                entity_item=entity,
                coordinator=coordinator,
                idx=index,
            )
            entries.append(mybutton)
            index += 1

    async_add_entities(
        entries,
        update_before_add=True,
    )


class MyButtonEntity(CoordinatorEntity, ButtonEntity, MyEntity):
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
        log.info("Button %s pressed", self._entity_item.translation_key)
        if self._entity_item.translation_key == TRANSLATION_KEY_SET_STANDBY_OFF:
            await self._rest_api.async_set_waterstop_standby(on_off_command=START)
        elif self._entity_item.translation_key == TRANSLATION_KEY_SET_STANDBY_ON:
            await self._rest_api.async_set_waterstop_standby(on_off_command=STOP)
        elif self._entity_item.translation_key == COMMAND_REGENERATION:
            await self.async_regerate()
        elif self._entity_item.translation_key == TRANSLATION_KEY_SET_STANDBY_OFF:
            await self._rest_api.async_turn_the_water(parameter=CLOSE)
        elif self._entity_item.translation_key == TRANSLATION_KEY_SET_STANDBY_ON:
            await self._rest_api.async_turn_the_water(parameter=OPEN)
        elif (
            self._entity_item.translation_key
            == TRANSLATION_KEY_OF_NORMAL_WATEROPERATION
        ):
            await self._rest_api.async_set_waterstop_standby(on_off_command=STOP)
            await self._rest_api.async_set_residual_waterhardness(10)
        elif self._entity_item.translation_key in (
            TRANSLATION_KEY_OF_GARTEN_IRRIGATION,
            TRANSLATION_KEY_OF_POOL_FILL_UP,
        ):
            await self._rest_api.async_set_waterstop_standby(on_off_command=START)
            await self._rest_api.async_set_residual_waterhardness(20)
        elif (
            self._entity_item.translation_key
            == TRANSLATION_KEY_OF_REFILL_BOILER_HEATING
        ):
            await self._rest_api.async_set_waterstop_standby(on_off_command=START)
            await self._rest_api.async_set_residual_waterhardness(5)

    async def async_regerate(self) -> None:
        """Start the regeneration."""
        if await self._rest_api.async_get_is_judo_regenerate():
            logging.getLogger(__name__).info("Regeneration is already running.")
        else:
            await self._rest_api.async_set_regeneration()
