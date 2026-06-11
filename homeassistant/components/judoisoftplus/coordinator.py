"""Coordinator for Project."""

from datetime import timedelta
import logging

from homeassistant.const import CONF_SCAN_INTERVAL
from homeassistant.core import HomeAssistant
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator

from .configentry import MyConfigEntry
from .const import (
    COMMAND_NATURAL_WATERHARDNESS,
    COMMAND_REGENERATION,
    COMMAND_RESIDUAL_WATERHARDNESS,
    COMMAND_SALT_QUANTITY,
    COMMAND_SALT_RANGE,
    COMMAND_STANDBY,
    COMMAND_TURN_ON_OF_THE_WATER,
    COMMAND_WATER_AVERAGE,
    COMMAND_WATER_CURRENT,
    COMMAND_WATER_TOTAL,
)
from .item import Item
from .judoisoftplusrestservice import JudoRestAPI

logging.basicConfig()
log = logging.getLogger(__name__)


class MyCoordinator(DataUpdateCoordinator):
    """My custom coordinator."""

    def __init__(
        self,
        hass: HomeAssistant,
        my_api: JudoRestAPI,
        api_items: list[Item],
        config_entry: MyConfigEntry,
    ) -> None:
        """Initialize my coordinator."""
        super().__init__(
            hass,
            log,
            # Name of the data. For logging purposes.
            name="judo_rest_api_coordinator",
            # Polling interval. Will only be polled if there are subscribers.
            # update_interval=CONST.SCAN_INTERVAL,
            update_interval=timedelta(
                seconds=int(config_entry.data[CONF_SCAN_INTERVAL]),
            ),
            always_update=True,
        )
        self._rest_api = my_api
        self._device = None
        self._restitems = api_items
        self._config_entry = config_entry
        self._number_of_entities = sum(len(item.list_of_entites) for item in api_items)

    async def get_value(self, rest_item: Item):
        """Read a value from the rest API."""
        log.info("Getting value for item: %s", rest_item.rest_item_name)
        data = []
        if rest_item.rest_item_name == COMMAND_WATER_AVERAGE:
            data.append(await self._rest_api.async_get_average_water_consumption())
        elif rest_item.rest_item_name == COMMAND_WATER_CURRENT:
            temporary_data = str(
                await self._rest_api.async_get_current_water_consumption()
            )
            data.extend(temporary_data.split())
        elif rest_item.rest_item_name == COMMAND_WATER_TOTAL:
            temporary_data = str(
                await self._rest_api.async_get_total_water_consumption()
            )
            data.extend(temporary_data.split())
        elif rest_item.rest_item_name == COMMAND_SALT_QUANTITY:
            log.info("Getting salt quantity")
            temporary_data = int(str(await self._rest_api.async_salt_quantity())) / 1000
            data.append(temporary_data)
            data.append(str(float(temporary_data) * 100 / 50))
        elif rest_item.rest_item_name == COMMAND_SALT_RANGE:
            temporary_data = str(await self._rest_api.async_get_salt_range())
            temporary_int = int(temporary_data)
            data.append(temporary_data)
            data.append(str(round(temporary_int / 7)))
        elif rest_item.rest_item_name == COMMAND_STANDBY:
            data.append(
                "on"
                if await self._rest_api.async_get_waterstop_standby() == "0"
                else "off"
            )
        elif rest_item.rest_item_name == COMMAND_NATURAL_WATERHARDNESS:
            data.append(await self._rest_api.async_get_natural_water_hardness())
        elif rest_item.rest_item_name == COMMAND_RESIDUAL_WATERHARDNESS:
            data.append(await self._rest_api.async_get_residual_water_hardness())
        elif rest_item.rest_item_name == COMMAND_REGENERATION:
            data.append(
                "True"
                if await self._rest_api.async_get_is_judo_regenerate()
                else "False"
            )
        elif rest_item.rest_item_name == COMMAND_TURN_ON_OF_THE_WATER:
            data.append(await self._rest_api.async_current_water_valve())
        else:
            log.error("Unknown item: %s", rest_item.rest_item_name)
            return data
        return data

    async def _async_setup(self):
        """Set up the coordinator."""
        await self._rest_api.async_login_and_connect()

    async def _async_update_data(self):
        """Fetch data from API endpoint.

        This is the place to pre-process the data to lookup tables
        so entities can quickly look up their data.
        """
        for rest_item in self._restitems:
            data = await self.get_value(rest_item)
            if len(rest_item.list_of_entites) > 1:
                rest_item.list_of_entites[0].result = data[0]
                rest_item.list_of_entites[1].result = data[1]
            else:
                rest_item.list_of_entites[0].result = data[0]
        return self._restitems

    @property
    def rest_api(self):
        """Return rest_api."""
        return self._rest_api
