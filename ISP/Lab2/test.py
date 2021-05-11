from serializer_lib.factory.factory import create_serializer
from serializer_lib.serializers.json_serializer import JSONSerializer

a = {
    "a": 1,
    "b": "stroka",
    "c": (1, 2, 3),
}

print(a)
ser = create_serializer("json")
json = ser.dumps(a)
print(json)
b = ser.loads(json)
print(b)