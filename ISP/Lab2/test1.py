from serializer_lib.factory.factory import create_serializer
from tests.test_main import *


from serializer_lib.parsers.yaml_parser import to_yaml, from_yaml
from serializer_lib.parsers.json_parser import from_json


def f(x):
    return x*x


ser = create_serializer("json")
ser.dump(f, "my_tests/func.json")



