from prothon.proto_base import ProtoBase


class ProtoField(ProtoBase):
    def __init__(self, option, data_type, name, index):
        self.__option = option
        self.__data_type = data_type
        self.__name = name
        self.__index = index

    def make(self):
        return '\t{} {} {} = {};\n'.format(self.__option, self.__data_type, self.__name, self.__index)
