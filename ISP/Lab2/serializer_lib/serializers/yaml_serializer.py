from .serializer import Serializer
from serializer_lib.serialization.serialization import serialize, deserialize
from serializer_lib.parsers.yaml_parser import to_yaml, from_yaml


class YAMLSerializer(Serializer):
    def dumps(self, obj):
        return to_yaml(serialize(obj))

    def loads(self, s):
        return deserialize(from_yaml(s))

    def dump(self, obj, fp):
        fp.write(self.dumps(obj))

    def load(self, fp):
        return self.loads(fp.read())


