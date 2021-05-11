from serializer_lib.serializers.serializer import Serializer
from serializer_lib.serializers.json_serializer import JSONSerializer


def create_serializer(format_name):
    format_name.lower()
    if format_name == "json":
        return JSONSerializer()
