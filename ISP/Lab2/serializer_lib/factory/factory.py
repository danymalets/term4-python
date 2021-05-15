from serializer_lib.serializers.serializer import Serializer
from serializer_lib.serializers.json_serializer import JSONSerializer
from serializer_lib.serializers.toml_serializer import TOMLSerializer
from serializer_lib.serializers.yaml_serializer import YAMLSerializer
from serializer_lib.serializers.pickle_serializer import PICKLESerializer


def create_serializer(format_name):
    format_name = format_name.lower()
    if format_name == "json":
        return JSONSerializer()
    elif format_name == "toml":
        return TOMLSerializer()
    elif format_name == "yaml":
        return YAMLSerializer()
    elif format_name == "pickle":
        return PICKLESerializer()
    else:
        raise ValueError(f"Wrong format {format_name}")
