from .serializer import Serializer
from serializer_lib.serialization.serialization import serialize, deserialize
from serializer_lib.parsers.pickle_parser import to_pickle, from_pickle


class PICKLESerializer(Serializer):
    def dumps(self, obj):
        return to_pickle(serialize(obj))

    def loads(self, s):
        return deserialize(from_pickle(s))

    def dump(self, obj, fp):
        fp.write(self.dumps(obj))

    def load(self, fp):
        return self.loads(fp.read())


