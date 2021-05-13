from yaml import dump as dumps, full_load as loads


def to_yaml(obj):
    return dumps(obj)


def from_yaml(s):
    return loads(s)