from serializer_lib.factory.factory import create_serializer
import logging

ser = create_serializer("json")
func = ser.load("my_tests/func.json")
print(func(5))