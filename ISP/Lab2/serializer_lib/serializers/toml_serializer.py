from .serializer import Serializer
from serializer_lib.serialization.serialization import serialize, deserialize
from serializer_lib.parsers.toml_parser import to_toml, from_toml


class TOMLSerializer(Serializer):
    def dumps(self, obj):
        return to_toml(serialize(obj))

    def loads(self, s):
        return deserialize(from_toml(s))

    def dump(self, obj, fp):
        fp.write(self.dumps(obj))

    def load(self, fp):
        return self.loads(fp.read())


