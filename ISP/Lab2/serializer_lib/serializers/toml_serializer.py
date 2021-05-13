from .serializer import Serializer
from serializer_lib.serialization.serialization import serialize, deserialize
from serializer_lib.parsers.json_parser import to_json, from_json


import json


class JSONSerializer(Serializer):
    def dumps(self, obj):
        return to_json(serialize(obj))

    def loads(self, s):
        print("ans = " + s)
        print("ans1 = " + str(from_json(s)))
        print("ans2 = " + str(json.loads(s)))
        return deserialize(from_json(s))

    def dump(self, obj, fp):
        fp.write(self.dumps(obj))

    def load(self, fp):
        return self.loads(fp.read())


