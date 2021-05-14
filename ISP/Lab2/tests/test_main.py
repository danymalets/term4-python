from serializer_lib.factory.factory import create_serializer
from .test_funcs import *


JSON_DICT = "tests/test_dict.json"


def test_json_dict():
    ser = create_serializer("json")
    a = {"a": 1, "b": 2, "c": (False, True, None, [12.32]), "d1": []}

    with open(JSON_DICT, 'w') as fp:
        ser.dump(a, fp)

    with open(JSON_DICT, 'r') as fp:
        b = ser.load(fp)

    assert a == b


def test_json_fib():
    ser = create_serializer("json")
    s = ser.dumps(fib)
    new_fib = ser.loads(s)

    assert fib(5) == new_fib(5)


def test_json_func():
    ser = create_serializer("json")
    s = ser.dumps(func)
    new_func = ser.loads(s)

    assert func(30) == new_func(30)


def test_json_strings():
    ser = create_serializer("JSON")
    a = ["qwijfc23mkqwdf", "dany\nmalets", "qwe\\rty", "123/456", "", "a\\\n\/"]
    s = ser.dumps(a)
    b = ser.loads(s)
    assert a == b