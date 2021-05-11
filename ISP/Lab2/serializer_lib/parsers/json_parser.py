from json import dumps, loads


def to_json(obj):
    return dumps(obj)


def from_json(s):
    return loads(s)
