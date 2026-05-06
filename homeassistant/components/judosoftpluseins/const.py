"""Constants for the Judo Soft Plus Eins integration."""

from homeassistant.const import CONF_SENSOR_TYPE

from .item import Item

DOMAIN = "judosoftpluseins"
DEVICE = "i-soft plus"

"""Constants for the Judo (Rest-Service i-soft plus) integration."""
GROUP_REGISTER = "register"
GROUP_SPARE = "spare"
GROUP_WATERSTOP = "waterstop"
GROUP_INFO = "info"
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
COMMAND_WATER_YEARLY = "water yearly"
COMMAND_WATER_CURRENT = "water current"
COMMAND_WATER_MONTHLY = "water monthly"
COMMAND_WATER_DAILY = "water daily"
COMMAND_WATER_WEEKLY = "water weekly"
COMMAND_SALT_QUANTITY = "salt quantity"
COMMAND_SALT_RANGE = "salt range"
COMMAND_LOGIN = "login"
COMMAD_LOGOUT = "logout"
COMMAND_CONNECT = "connect"
COMMAND_DISCONNECT = "disconnect"
COMMAND_STANDBY = "standby"
"""For RestService Waterstop Standby-Parameter"""
COMMAND_WATERSTOP_START = "start"
COMMAND_WATERSTOP_STOP = "stop"
"""For RestService Status"""
STATUS_OK = "ok"
STATUS_FAILED = "failed"
STATUS = "status"
TITLE = "title"

"""For output"""
DAYS = "Days"
LITER = "Liter"

REST_ITEMS: list[Item] = [
    Item(translation_key="water_yearly", icon="mdi:water", format=CONF_SENSOR_TYPE),
    Item(translation_key="water_monthly", icon="mdi:water", format=CONF_SENSOR_TYPE),
    Item(translation_key="water_daily", icon="mdi:water", format=CONF_SENSOR_TYPE),
    Item(translation_key="water_weekly", icon="mdi:water", format=CONF_SENSOR_TYPE),
    Item(translation_key="salt_quantity", icon="mdi:salt", format=CONF_SENSOR_TYPE),
    Item(translation_key="salt_range", icon="mdi:salt", format=CONF_SENSOR_TYPE),
]
