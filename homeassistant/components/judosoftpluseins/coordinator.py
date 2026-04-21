"""Coordinator for Project."""

from datetime import timedelta
import logging

from homeassistant import const
from homeassistant.core import HomeAssistant
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator

from .configentry import MyConfigEntry
from .const import COMMAND_SALT_QUANTITY, COMMAND_SALT_RANGE
from .item import Item
from .judopluseinsrestservice import JudoRestAPI

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
            name="judo_rest_api-coordinator",
            # Polling interval. Will only be polled if there are subscribers.
            # update_interval=CONST.SCAN_INTERVAL,
            update_interval=timedelta(
                seconds=int(config_entry.data[const.CONF_SCAN_INTERVAL])
            ),
            # Set always_update to `False` if the data returned from the
            # api can be compared via `__eq__` to avoid duplicate updates
            # being dispatched to listeners
            always_update=True,
        )
        self._rest_api = my_api
        self._device = None
        self._restitems = api_items
        self._number_of_items = len(api_items)
        self._config_entry = config_entry

    async def get_value(self, rest_item: Item):
        """Read a value from the rest API."""
        match rest_item.translation_key:
            case "water_yearly":
                data = await self._rest_api.async_get_water_consumtion_of_year()
            case "water_monthly":
                data = await self._rest_api.async_get_water_consumtion_of_month()
            case "water_daily":
                data = await self._rest_api.async_get_water_consumtion_of_day()
            case "water_weekly":
                data = await self._rest_api.async_get_water_consumtion_of_week()
            case "salt_quantity":
                data = await self._rest_api.async_get_salt_consumption_request(
                    command=COMMAND_SALT_QUANTITY
                )
            case "salt_range":
                data = await self._rest_api.async_get_salt_consumption_request(
                    command=COMMAND_SALT_RANGE
                )
            case _:
                log.error("Unknown item: %s", rest_item.translation_key)
                return 0
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
            rest_item.value = str(await self.get_value(rest_item))

    @property
    def rest_api(self):
        """Return rest_api."""
        return self._rest_api
