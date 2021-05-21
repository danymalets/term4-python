from serializer_lib.factory.factory import create_serializer
from .test_source import *


JSON_DICT = "tests/test_dict.json"
PICKLE_DICT = "tests/test_dict.pickle"
YAML_DICT = "tests/test_dict.yaml"
TOML_DICT = "tests/test_dict.toml"


def test_json_dict():
    ser = create_serializer("json")
    a = {"a": 1, "b": 2, "c": (False, True, None, [12.32]), "d1": []}

    ser.dump(a, JSON_DICT)

    b = ser.load(JSON_DICT)

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


def test_pickle_dict():
    ser = create_serializer("pickle")
    a = {"a": 1, "b": 2, "c": 3}
    bts = ser.dumps(a)
    b = ser.loads(bts)
    assert a == b


def test_pickle_file():
    ser = create_serializer("pickle")
    a = {"a": 1, "b": 2, "c": 3}
    ser.dump(a, PICKLE_DICT)
    b = ser.load(PICKLE_DICT)
    assert a == b


def test_yaml():
    ser = create_serializer("yaml")
    a = {"a": 1, "b": 2.2, "c": False, "d": True, "e": None, "f1": [1, 2, 3]}
    s = ser.dumps(a)

    b = ser.loads(s)
    assert a == b


def test_toml():
    ser = create_serializer("toml")
    a = {"a": 1, "b": 2.2, "c": False, "d": True, "f1": [1, 2, 3]}
    s = ser.dumps(a)
    b = ser.loads(s)
    assert a == b


def test_yaml_file():
    ser = create_serializer("yaml")
    a = {"a": 1, "b": 2.2, "c": False, "d": True, "e": None, "f1": [1, 2, 3]}
    ser.dump(a, YAML_DICT)
    b = ser.load(YAML_DICT)
    assert a == b


def test_toml_file():
    ser = create_serializer("toml")
    a = {"a": 1, "b": 2.2, "c": False, "d": True, "f1": [1, 2, 3]}
    ser.dump(a, TOML_DICT)
    b = ser.load(TOML_DICT)
    assert a == b


def test_class():
    ser = create_serializer("json")
    s = ser.dumps(A)
    B = ser.loads(s)
    assert A.a == B.a


def test_obj():
    ser = create_serializer("json")
    a = A()
    s = ser.dumps(a)
    b = ser.loads(s)
    assert a.a == b.a
    assert a.sqr(5) == b.sqr(5)


def test_complex_dict():
    ser = create_serializer("json")
    a = {"a": 1, "b": 2.2, 3: 9, False: True}
    s = ser.dumps(a)
    b = ser.loads(s)
    assert a == b
