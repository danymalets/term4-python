import re
from toml import dumps, loads

FLOAT_REGEX = "-?[\d]+\.[\d]+"
INT_REGEX = "^-?[\d]+$"


def to_toml(obj):
    return dumps(obj)


def from_toml(s):
    return loads(s)