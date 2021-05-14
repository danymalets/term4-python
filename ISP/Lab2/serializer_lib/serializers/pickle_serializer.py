from .serializer import Serializer
from serializer_lib.serialization.serialization import serialize, deserialize
import pickle as pc


class PICKLESerializer(Serializer):
    def dumps(self, obj):
        return pc.dumps(serialize(obj))

    def loads(self, s):
        return deserialize(pc.loads(s))

    def dump(self, obj, file_path):
        with open(file_path, 'wb') as fp:
            pc.dump(serialize(obj), fp)

    def load(self, file_path):
        with open(file_path, 'rb') as fp:
            return deserialize(pc.load(fp))


