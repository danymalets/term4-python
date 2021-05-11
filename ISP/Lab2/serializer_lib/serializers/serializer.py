from abc import ABC, abstractmethod


class Serializer(ABC):
    @abstractmethod
    def dumps(self, obj):
        pass

    @abstractmethod
    def loads(self, s):
        pass

    @abstractmethod
    def dump(self, obj, fp):
        pass

    @abstractmethod
    def load(self, fp):
        pass


