from .serializer import Serializer
from serializer_lib.serialization.serialization import serialize, deserialize
from serializer_lib.parsers.json_parser import to_json, from_json


class JSONSerializer(Serializer):
    def dumps(self, obj):
        return to_json(serialize(obj))

    def loads(self, s):
        return deserialize(from_json(s))

    def dump(self, obj, file_path):
        with open(file_path, 'w') as fp:
            fp.write(self.dumps(obj))

    def load(self, file_path):
        with open(file_path, 'r') as fp:
            return self.loads(fp.read())


