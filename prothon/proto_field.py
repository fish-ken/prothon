from prothon.proto_base import ProtoBase


class ProtoField(ProtoBase):
    def __init__(self, option, data_type, name, index):
        self.__option = option
        self.__data_type = data_type
        self.__name = name
        self.__index = index
        self.__initialize()

    def __initialize(self):
        if self.__data_type is 'enum':
            self.__data_type = self.__name

    def make(self):
        if self.__option is None:
            return '\t{} {} = {};\n'.format(self.__data_type, self.__name, self.__index)
        else:
            return '\t{} {} {} = {};\n'.format(self.__option, self.__data_type, self.__name, self.__index)
