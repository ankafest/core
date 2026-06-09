"""Scene of judosoftpluseins integration."""

import logging
from typing import Any

from homeassistant.components.scene import BaseScene
from homeassistant.core import HomeAssistant
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback
from homeassistant.helpers.update_coordinator import CoordinatorEntity

from .configentry import MyConfigEntry
from .const import COMMAND_RESIDUAL_WATERHARDNESS, COMMAND_STANDBY, SCENE_ITEMS
from .coordinator import MyCoordinator
from .entity import EntityItem, MyEntity
from .entity_item import EntityItem
from .scene_item import SceneItem


async def async_setup_entry(
    hass: HomeAssistant,
    config_entry: MyConfigEntry,
    async_add_entities: AddConfigEntryEntitiesCallback,
) -> None:
    """Start with an empty list of entries."""
    entries = []

    coordinator = config_entry.runtime_data.coordinator
    index = 0
    for item in SCENE_ITEMS:
        myscene = MyScene(
            config_entry=config_entry,
            scene_item=item,
            coordinator=coordinator,
            idx=index,
        )
        entries.append(myscene)
        index += 1

    async_add_entities(
        entries,
        update_before_add=True,
    )


class MyScene(CoordinatorEntity, BaseScene, MyEntity):
    """Scenes for judosoftpluseins integration."""

    def __init__(
        self,
        config_entry: MyConfigEntry,
        scene_item: SceneItem,
        coordinator: MyCoordinator,
        idx: int,
    ) -> None:
        """Init the scene."""
        super().__init__(coordinator)
        self._entity_id = scene_item.scene_name
        self._config_entry = config_entry
        self._scene_item = scene_item
        self._rest_api = coordinator._rest_api
        self._idx = idx
        self._entity_item = EntityItem(
            translation_key=scene_item.scene_name,
            icon=self._scene_item.icon,
            unit="scene",
        )
        MyEntity.__init__(self, config_entry, self._entity_item, coordinator.rest_api)

    async def async_activate(self, **kwargs: Any) -> None:
        """Activate scene. Try to get entities into requested state."""
        for rest_command in self._scene_item.list_of_rest_commands:
            if rest_command.rest_command == COMMAND_RESIDUAL_WATERHARDNESS:
                await self._rest_api.async_set_residual_waterhardness(
                    rest_command.value
                )
            elif rest_command.rest_command == COMMAND_STANDBY:
                await self._rest_api.async_set_waterstop_standby(rest_command.value)
