"""Common constants. Do not use them directly, all public ones are imported to __init__.py"""

from enum import IntEnum
from typing import TypedDict


class LogLvl(IntEnum):
    DEBUG = 0
    INFO = 1
    WARNING = 2
    ERROR = 3
    FATAL = 4


APP_V2_BASIC_URL = "/ocs/v1.php/apps/app_ecosystem_v2/api/v1"


class ApiScope(IntEnum):
    SYSTEM = 2
    DAV = 3
    USER_INFO = 10
    USER_STATUS = 11
    NOTIFICATIONS = 12
    WEATHER_STATUS = 13


class ApiScopesStruct(TypedDict):
    required: list[int]
    optional: list[int]


class OCSRespond(IntEnum):
    RESPOND_SERVER_ERROR = 996
    RESPOND_UNAUTHORISED = 997
    RESPOND_NOT_FOUND = 998
    RESPOND_UNKNOWN_ERROR = 999
