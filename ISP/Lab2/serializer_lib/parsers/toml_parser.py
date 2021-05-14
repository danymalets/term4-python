import re
from toml import dumps, loads


def to_toml(obj):
    return dumps(obj)


def from_toml(s):
    return loads(s)