import re
from toml import dumps, loads


import re

FLOAT_REGEX = "-?\d+\.\d+"
INT_REGEX = "\d+"
STR_REGEX = "\"(.*)\""
LIST_REGEX = "\[([\s\S]*)\]"


def to_toml(obj):
    return dumps(obj)


def from_toml(s):
    return loads(s)
