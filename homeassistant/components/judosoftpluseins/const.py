"""Constants for the Judo Soft Plus Eins integration."""

from homeassistant.const import PERCENTAGE, UnitOfMass, UnitOfVolume

from .entity_item import EntityItem
from .item import Item

DOMAIN = "judosoftpluseins"
DEVICE = "i-soft plus"

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
DEFAULT_DEVICE = "i-soft plus"
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
COMMAD_LOGOUT = "logout"
COMMAND_CONNECT = "connect"
COMMAND_DISCONNECT = "disconnect"
COMMAND_STANDBY = "standby"
COMMAND_NATURAL_WATERHARDNESS = "natural hardness"
COMMAND_RESIDUAL_WATERHARDNESS = "residual hardness"
STANDBY_ON = "standby on"
STANDBY_OFF = "standby off"
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
"""For RestService Waterstop Standby-Parameter"""
COMMAND_START = "start"
COMMAND_STOP = "stop"
"""For RestService Status"""
STATUS_OK = "ok"
STATUS_FAILED = "failed"
STATUS = "status"
TITLE = "title"
REGENERATE = "regenerate"

"""For Types of Entites"""
SENSOR_TYPE = "sensor"
BUTTON_TYPE = "button"
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
        format=SENSOR_TYPE,
        unit=LITER,
    )
]

LIST_OF_CURRENT_WATTER_CONSUMPTION: list[EntityItem] = [
    EntityItem(
        translation_key=TRANSLATION_KEY_CURRENT_WATER_RAW,
        icon="mdi:water",
        format=SENSOR_TYPE,
        unit=LITER,
    ),
    EntityItem(
        translation_key=TRANSLATION_KEY_CURRENT_WATER_SOFT,
        icon="mdi:water",
        format=SENSOR_TYPE,
        unit=LITER,
    ),
]

LIST_OF_TOTAL_WATTER_CONSUMPTION: list[EntityItem] = [
    EntityItem(
        translation_key=TRANSLATION_KEY_TOTAL_WATER_RAW,
        icon="mdi:water",
        format=SENSOR_TYPE,
        unit=LITER,
    ),
    EntityItem(
        translation_key=TRANSLATION_KEY_TOTAL_WATER_SOFT,
        icon="mdi:water",
        format=SENSOR_TYPE,
        unit=LITER,
    ),
]

LIST_OF_SALT_QUANTITY: list[EntityItem] = [
    EntityItem(
        translation_key=TRANSLATION_KEY_SALT_QUANTITY,
        icon="mdi:water-opacity",
        format=SENSOR_TYPE,
        unit=KILOGRAM,
    ),
    EntityItem(
        translation_key=TRANSLATION_KEY_SALT_QUANTITY_PERCENT,
        icon="mdi:water-percent",
        format=SENSOR_TYPE,
        unit=PERCENT,
    ),
]

LIST_OF_SALT_RANGE: list[EntityItem] = [
    EntityItem(
        translation_key=TRANSLATION_KEY_SALT_RANGE_DAYS,
        icon="mdi:water-opacity",
        format=SENSOR_TYPE,
        unit=DAYS,
    ),
    EntityItem(
        translation_key=TRANSLATION_KEY_SALT_RANGE_WEEKS,
        icon="mdi:water-opacity",
        format=SENSOR_TYPE,
        unit=WEEKS,
    ),
]

LIST_OF_STANDBY_MODE: list[EntityItem] = [
    EntityItem(
        translation_key=TRANSLATION_KEY_STANDBY_MODE,
        icon="mdi:water-off",
        format=SENSOR_TYPE,
        unit=" ",
    )
]

LIST_OF_STANDBY_MODE_ON: list[EntityItem] = [
    EntityItem(
        translation_key=TRANSLATION_KEY_SET_STANDBY_ON,
        icon="mdi:water",
        format=BUTTON_TYPE,
        unit=" ",
    )
]

LIST_OF_IS_REGENERATING_RUNNING: list[EntityItem] = [
    EntityItem(
        translation_key=TRANSLATION_IS_REGENERATING_RUNNING,
        icon="mdi:water-polo",
        format=SENSOR_TYPE,
        unit=" ",
    )
]

LIST_OF_STANDBY_MODE_OFF: list[EntityItem] = [
    EntityItem(
        translation_key=TRANSLATION_KEY_SET_STANDBY_OFF,
        icon="mdi:water-remove",
        format=BUTTON_TYPE,
        unit=" ",
    )
]

LIST_OF_NATURAL_WATERHARDNESS: list[EntityItem] = [
    EntityItem(
        translation_key=TRANSLATION_KEY_NATURAL_WATERHARDNESS,
        icon="mdi:water-opacity",
        format=SENSOR_TYPE,
        unit="dH",
    )
]

LIST_OF_RESIDUAL_WATERHARDNESS: list[EntityItem] = [
    EntityItem(
        translation_key=TRANSLATION_KEY_RESIDUAL_WATERHARDNESS,
        icon="mdi:water-opacity",
        format=SENSOR_TYPE,
        unit="dH",
    )
]

LIST_OF_WATERREGENERATION: list[EntityItem] = [
    EntityItem(
        translation_key=COMMAND_REGENERATION,
        icon="mdi:water-polo",
        format=BUTTON_TYPE,
        unit=" ",
    )
]

REST_ITEMS: list[Item] = [
    Item(
        rest_item_name=COMMAND_WATER_CURRENT,
        list_of_entites=LIST_OF_CURRENT_WATTER_CONSUMPTION,
    ),
    Item(
        rest_item_name=COMMAND_WATER_AVERAGE,
        list_of_entites=LIST_OF_ENTITYS_FOR_WATER_AVERAGE,
    ),
    Item(
        rest_item_name=COMMAND_WATER_TOTAL,
        list_of_entites=LIST_OF_TOTAL_WATTER_CONSUMPTION,
    ),
    Item(rest_item_name=COMMAND_SALT_QUANTITY, list_of_entites=LIST_OF_SALT_QUANTITY),
    Item(rest_item_name=COMMAND_SALT_RANGE, list_of_entites=LIST_OF_SALT_RANGE),
    Item(rest_item_name=COMMAND_STANDBY, list_of_entites=LIST_OF_STANDBY_MODE),
    Item(
        rest_item_name=COMMAND_NATURAL_WATERHARDNESS,
        list_of_entites=LIST_OF_NATURAL_WATERHARDNESS,
    ),
    Item(
        rest_item_name=COMMAND_RESIDUAL_WATERHARDNESS,
        list_of_entites=LIST_OF_RESIDUAL_WATERHARDNESS,
    ),
    Item(
        rest_item_name=COMMAND_REGENERATION,
        list_of_entites=LIST_OF_IS_REGENERATING_RUNNING,
    ),
]

BUTTON_ITEMS: list[Item] = [
    Item(
        rest_item_name=STANDBY_ON,
        list_of_entites=LIST_OF_STANDBY_MODE_ON,
    ),
    Item(
        rest_item_name=STANDBY_OFF,
        list_of_entites=LIST_OF_STANDBY_MODE_OFF,
    ),
    Item(
        rest_item_name=COMMAND_REGENERATION, list_of_entites=LIST_OF_WATERREGENERATION
    ),
]
