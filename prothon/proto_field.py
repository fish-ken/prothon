from prothon.proto_base import ProtoBase


class ProtoField(ProtoBase):
    def __init__(self, option, data_type, name, index):
        self.__option = option
        self.__data_type = data_type
        self.__name = name
        self.__index = index
        self.__initialize()

    def __initialize(self):
        if self.__data_type == 'enum':
            self.__data_type = self.__name
        self.__name = self.__name[0].lower() + self.__name[1:]

    def make(self):
        if self.__option is None:
            return '{} {} = {};'.format(self.__data_type, self.__name, self.__index)
        else:
            return '{} {} {} = {};'.format(self.__option, self.__data_type, self.__name, self.__index)
