from serializer_lib.factory.factory import create_serializer
from tests.test_main import *

ser = create_serializer("json")
a = ser.load("my_tests/data.json")


ser = create_serializer("yaml")
ser.dump(a, "my_tests/data.yaml")
