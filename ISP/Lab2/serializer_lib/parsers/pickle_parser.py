from pickle import dumps, loads


def to_pickle(obj):
    return dumps(obj)


def from_pickle(bts):
    return loads(bts)