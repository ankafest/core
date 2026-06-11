"""Constants for the Judo Soft Plus Eins integration."""

from homeassistant.const import PERCENTAGE, UnitOfMass, UnitOfVolume

from .entity_item import EntityItem
from .item import Item

DOMAIN = "judoisoftplus"
DEVICE = "Judo iSoft plus"

"""Constants for the Judo (Rest-Service i-soft plus) integration."""
GROUP_REGISTER = "register"
GROUP_SPARE = "spare"
GROUP_WATERSTOP = "waterstop"
GROUP_INFO = "info"
GROUP_SETTINGS = "settings"
GROUP_CONSUMPTION = "consumption"
"""For Restservice various necessary information"""
GROUP = "group"
COMMAND = "command"
PARAMETER = "parameter"
TOKEN = "token"
ROLE = "role"
ROLE_CUSTOMER = "customer"
DEFAULT_DEVICE = "Judo iSoft plus"
DEVICE_FOR_CONNECT = "i-soft plus"
SERIAL_NUMBER = "serial number"
USER = "user"
DAY = "day"
MONTH = "month"
WEEK = "week"
YEAR = "year"
DATA = "data"
"""For RestService command"""
COMMAND_WATER_CURRENT = "water current"
COMMAND_WATER_AVERAGE = "water average"
COMMAND_WATER_TOTAL = "water total"
COMMAND_WATER_YEARLY = "water yearly"
COMMAND_WATER_CURRENT = "water current"
COMMAND_SALT_QUANTITY = "salt quantity"
COMMAND_REGENERATION = "regeneration"
COMMAND_SALT_RANGE = "salt range"
COMMAND_LOGIN = "login"
COMMAND_LOGOUT = "logout"
COMMAND_CONNECT = "connect"
COMMAND_DISCONNECT = "disconnect"
COMMAND_STANDBY = "standby"
COMMAND_NATURAL_WATERHARDNESS = "natural hardness"
COMMAND_RESIDUAL_WATERHARDNESS = "residual hardness"
COMMAND_TURN_ON_OF_THE_WATER = "valve"
STANDBY_ON = "standby on"
STANDBY_OFF = "standby off"
TURN_OFF_THE_WATER = "turn off the water"
TURN_ON_THE_WATER = "turn on the water"
TRANSLATION_IS_REGENERATING_RUNNING = "is_regenerating_running"
TRANSLATION_KEY_WATER_AVERAGE = "water_average"
TRANSLATION_KEY_CURRENT_WATER_RAW = "currently_raw_water"
TRANSLATION_KEY_CURRENT_WATER_SOFT = "currently_soft_water"
TRANSLATION_KEY_TOTAL_WATER_RAW = "total_raw_water"
TRANSLATION_KEY_TOTAL_WATER_SOFT = "total_soft_water"
TRANSLATION_KEY_SALT_QUANTITY = "salt_quantity"
TRANSLATION_KEY_SALT_RANGE_DAYS = "salt_range_in_days"
TRANSLATION_KEY_SALT_RANGE_WEEKS = "salt_range_in_weeks"
TRANSLATION_KEY_SALT_QUANTITY_PERCENT = "salt_quantity_percent"
TRANSLATION_KEY_SALT_QUANTITY = "salt_quantity"
TRANSLATION_KEY_NATURAL_WATERHARDNESS = "natural_water_hardness"
TRANSLATION_KEY_RESIDUAL_WATERHARDNESS = "residual_water_hardness"
TRANSLATION_KEY_STANDBY_MODE = "standby_mode"
TRANSLATION_KEY_SET_STANDBY_ON = "set_standby_mode_on"
TRANSLATION_KEY_SET_STANDBY_OFF = "set_standby_mode_off"
TRANSLATION_KEY_TURN_OFF_THE_WATER = "turn_off_the_water"
TRANSLATION_KEY_TURN_ON_THE_WATER = "turn_on_the_water"
TRANSLATION_KEY_CURRENT_WATER_VALVE = "current_water_valve"
"""For RestService Waterstop Standby-Parameter"""
COMMAND_START = "start"
COMMAND_STOP = "stop"
"""For RestService Status"""
STATUS_OK = "ok"
STATUS_FAILED = "failed"
STATUS = "status"
TITLE = "title"
REGENERATE = "regenerate"
OPEN = "open"
CLOSE = "close"
START = "start"
STOP = "stop"
"""Scene name"""
TRANSLATION_KEY_OF_GARTEN_IRRIGATION = "garten_irrigation"
TRANSLATION_KEY_OF_POOL_FILL_UP = "pool_fill_up"
TRANSLATION_KEY_OF_REFILL_BOILER_HEATING = "refill_boiler_heating"
TRANSLATION_KEY_OF_NORMAL_WATEROPERATION = "normal_wateroperation"

"""For Types of Entites"""
SENSOR_TYPE = "sensor"
BUTTON_TYPE = "button"
NUMBER_TYPE = "number"
"""For output"""
DAYS = "d"
WEEKS = "w"
LITER = UnitOfVolume.LITERS
KILOGRAM = UnitOfMass.KILOGRAMS
PERCENT = PERCENTAGE

LIST_OF_ENTITYS_FOR_WATER_AVERAGE: list[EntityItem] = [
    EntityItem(
        translation_key=TRANSLATION_KEY_WATER_AVERAGE,
        icon="mdi:water",
        unit=LITER,
    )
]

LIST_OF_CURRENT_WATTER_CONSUMPTION: list[EntityItem] = [
    EntityItem(
        translation_key=TRANSLATION_KEY_CURRENT_WATER_RAW,
        icon="mdi:water",
        unit=LITER,
    ),
    EntityItem(
        translation_key=TRANSLATION_KEY_CURRENT_WATER_SOFT,
        icon="mdi:water",
        unit=LITER,
    ),
]

LIST_OF_TOTAL_WATTER_CONSUMPTION: list[EntityItem] = [
    EntityItem(
        translation_key=TRANSLATION_KEY_TOTAL_WATER_RAW,
        icon="mdi:water",
        unit=LITER,
    ),
    EntityItem(
        translation_key=TRANSLATION_KEY_TOTAL_WATER_SOFT,
        icon="mdi:water",
        unit=LITER,
    ),
]

LIST_OF_SALT_QUANTITY: list[EntityItem] = [
    EntityItem(
        translation_key=TRANSLATION_KEY_SALT_QUANTITY,
        icon="mdi:water-opacity",
        unit=KILOGRAM,
    ),
    EntityItem(
        translation_key=TRANSLATION_KEY_SALT_QUANTITY_PERCENT,
        icon="mdi:water-percent",
        unit=PERCENT,
    ),
]

LIST_OF_SALT_RANGE: list[EntityItem] = [
    EntityItem(
        translation_key=TRANSLATION_KEY_SALT_RANGE_DAYS,
        icon="mdi:water-opacity",
        unit=DAYS,
    ),
    EntityItem(
        translation_key=TRANSLATION_KEY_SALT_RANGE_WEEKS,
        icon="mdi:water-opacity",
        unit=WEEKS,
    ),
]

LIST_OF_STANDBY_MODE: list[EntityItem] = [
    EntityItem(
        translation_key=TRANSLATION_KEY_STANDBY_MODE,
        icon="mdi:water-off",
        unit=" ",
    )
]

LIST_OF_STANDBY_MODE_ON: list[EntityItem] = [
    EntityItem(
        translation_key=TRANSLATION_KEY_SET_STANDBY_ON,
        icon="mdi:water",
        unit=" ",
    )
]

LIST_OF_IS_REGENERATING_RUNNING: list[EntityItem] = [
    EntityItem(
        translation_key=TRANSLATION_IS_REGENERATING_RUNNING,
        icon="mdi:water-polo",
        unit=" ",
    )
]

LIST_OF_STANDBY_MODE_OFF: list[EntityItem] = [
    EntityItem(
        translation_key=TRANSLATION_KEY_SET_STANDBY_OFF,
        icon="mdi:water-remove",
        unit=" ",
    )
]

LIST_OF_NATURAL_WATERHARDNESS: list[EntityItem] = [
    EntityItem(
        translation_key=TRANSLATION_KEY_NATURAL_WATERHARDNESS,
        icon="mdi:water-opacity",
        unit="dH",
    )
]

LIST_OF_RESIDUAL_WATERHARDNESS: list[EntityItem] = [
    EntityItem(
        translation_key=TRANSLATION_KEY_RESIDUAL_WATERHARDNESS,
        icon="mdi:water-opacity",
        unit="dH",
    )
]

LIST_OF_GET_RESIDUAL_WATERHARDNESS: list[EntityItem] = [
    EntityItem(
        translation_key=TRANSLATION_KEY_RESIDUAL_WATERHARDNESS,
        icon="mdi:water-opacity",
        unit="dH",
    )
]


LIST_OF_WATERREGENERATION: list[EntityItem] = [
    EntityItem(
        translation_key=COMMAND_REGENERATION,
        icon="mdi:water-polo",
        unit=" ",
    )
]

LIST_OF_SET_RESIDUAL_WATERHARDNESS: list[EntityItem] = [
    EntityItem(
        translation_key=TRANSLATION_KEY_RESIDUAL_WATERHARDNESS,
        icon="mdi:water-opacity",
        unit="dH",
    )
]

LIST_OF_TURN_OFF_THE_WATER: list[EntityItem] = [
    EntityItem(
        translation_key=TRANSLATION_KEY_TURN_OFF_THE_WATER,
        icon="mdi:water-pump-off",
        unit=" ",
    )
]

LIST_OF_TURN_ON_THE_WATER: list[EntityItem] = [
    EntityItem(
        translation_key=TRANSLATION_KEY_TURN_ON_THE_WATER,
        icon="mdi:water-pump",
        unit=" ",
    )
]

LIST_OF_WATER_IRRIGATION: list[EntityItem] = [
    EntityItem(
        translation_key=TRANSLATION_KEY_OF_GARTEN_IRRIGATION,
        icon="mdi:watering-can",
        unit=" ",
    )
]

LIST_OF_REFILL_BOILER_HEATING: list[EntityItem] = [
    EntityItem(
        translation_key=TRANSLATION_KEY_OF_REFILL_BOILER_HEATING,
        icon="mdi:water-boiler",
        unit=" ",
    )
]

LIST_OF_POOL_FILL_UP: list[EntityItem] = [
    EntityItem(
        translation_key=TRANSLATION_KEY_OF_POOL_FILL_UP,
        icon="mdi:pool",
        unit=" ",
    )
]

LIST_OF_NORMAL_WATEROPERATION: list[EntityItem] = [
    EntityItem(
        translation_key=TRANSLATION_KEY_OF_NORMAL_WATEROPERATION,
        icon="mdi:water",
        unit=" ",
    )
]

LIST_OF_CURRENT_WATER_VALVE: list[EntityItem] = [
    EntityItem(
        translation_key=TRANSLATION_KEY_CURRENT_WATER_VALVE,
        icon="mdi:water",
        unit=" ",
    )
]

REST_ITEMS: list[Item] = [
    Item(
        rest_item_name=COMMAND_WATER_CURRENT,
        format=SENSOR_TYPE,
        list_of_entites=LIST_OF_CURRENT_WATTER_CONSUMPTION,
    ),
    Item(
        rest_item_name=COMMAND_WATER_AVERAGE,
        format=SENSOR_TYPE,
        list_of_entites=LIST_OF_ENTITYS_FOR_WATER_AVERAGE,
    ),
    Item(
        rest_item_name=COMMAND_WATER_TOTAL,
        format=SENSOR_TYPE,
        list_of_entites=LIST_OF_TOTAL_WATTER_CONSUMPTION,
    ),
    Item(
        rest_item_name=COMMAND_SALT_QUANTITY,
        format=SENSOR_TYPE,
        list_of_entites=LIST_OF_SALT_QUANTITY,
    ),
    Item(
        rest_item_name=COMMAND_SALT_RANGE,
        format=SENSOR_TYPE,
        list_of_entites=LIST_OF_SALT_RANGE,
    ),
    Item(
        rest_item_name=COMMAND_STANDBY,
        format=SENSOR_TYPE,
        list_of_entites=LIST_OF_STANDBY_MODE,
    ),
    Item(
        rest_item_name=COMMAND_NATURAL_WATERHARDNESS,
        format=SENSOR_TYPE,
        list_of_entites=LIST_OF_NATURAL_WATERHARDNESS,
    ),
    Item(
        rest_item_name=COMMAND_RESIDUAL_WATERHARDNESS,
        format=NUMBER_TYPE,
        list_of_entites=LIST_OF_SET_RESIDUAL_WATERHARDNESS,
    ),
    Item(
        rest_item_name=COMMAND_RESIDUAL_WATERHARDNESS,
        format=SENSOR_TYPE,
        list_of_entites=LIST_OF_GET_RESIDUAL_WATERHARDNESS,
    ),
    Item(
        rest_item_name=COMMAND_REGENERATION,
        format=SENSOR_TYPE,
        list_of_entites=LIST_OF_IS_REGENERATING_RUNNING,
    ),
    Item(
        rest_item_name=COMMAND_TURN_ON_OF_THE_WATER,
        format=SENSOR_TYPE,
        list_of_entites=LIST_OF_CURRENT_WATER_VALVE,
    ),
]

BUTTON_ITEMS: list[Item] = [
    Item(
        rest_item_name=STANDBY_ON,
        format=BUTTON_TYPE,
        list_of_entites=LIST_OF_STANDBY_MODE_ON,
    ),
    Item(
        rest_item_name=STANDBY_OFF,
        format=BUTTON_TYPE,
        list_of_entites=LIST_OF_STANDBY_MODE_OFF,
    ),
    Item(
        rest_item_name=COMMAND_REGENERATION,
        format=BUTTON_TYPE,
        list_of_entites=LIST_OF_WATERREGENERATION,
    ),
    Item(
        rest_item_name=TURN_OFF_THE_WATER,
        format=BUTTON_TYPE,
        list_of_entites=LIST_OF_TURN_OFF_THE_WATER,
    ),
    Item(
        rest_item_name=TURN_ON_THE_WATER,
        format=BUTTON_TYPE,
        list_of_entites=LIST_OF_TURN_ON_THE_WATER,
    ),
    Item(
        rest_item_name=TRANSLATION_KEY_OF_GARTEN_IRRIGATION,
        format=BUTTON_TYPE,
        list_of_entites=LIST_OF_WATER_IRRIGATION,
    ),
    Item(
        rest_item_name=TRANSLATION_KEY_OF_REFILL_BOILER_HEATING,
        format=BUTTON_TYPE,
        list_of_entites=LIST_OF_REFILL_BOILER_HEATING,
    ),
    Item(
        rest_item_name=TRANSLATION_KEY_OF_POOL_FILL_UP,
        format=BUTTON_TYPE,
        list_of_entites=LIST_OF_POOL_FILL_UP,
    ),
    Item(
        rest_item_name=TRANSLATION_KEY_OF_NORMAL_WATEROPERATION,
        format=BUTTON_TYPE,
        list_of_entites=LIST_OF_NORMAL_WATEROPERATION,
    ),
]
