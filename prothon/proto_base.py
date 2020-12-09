import abc


class ProtoBase(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def make(self):
        pass
