import openpyxl
from prothon.proto_base import ProtoBase
from prothon.proto_field import ProtoField

IGNORE_COLUMN_CHARACTER = '~'
MESSAGE_FORMAT = \
'message {0}\n\
{{\
\n\
    {1}\
\n\
    {2}\
\n\
}}'

class ProtoMessage(ProtoBase):
    """Protobuf message type class
    
    :param sheet : excel worksheet
    """

    def __init__(self, sheet:openpyxl.Worksheet):
        self.__sheet = sheet
        self.__name = self.__sheet.name
        self.__fields = []
        self.__messages = []
        self.__initialize()

    def __initialize(self):
        row_index = 2
        field_index = 0
        for column_index in range(len(self.__sheet[row_index])):
            column_name = self.__sheet[row_index][column_index].value

            if IGNORE_COLUMN_CHARACTER in column_name:
                continue 

            column_elements = column_name.split('[')

            # TODO : Variable option
            option = 'required'
            type_name = column_elements[1][:-1]
            name = column_elements[0]
            field_index += 1

            self.__fields.append(ProtoField(option, type_name, name, field_index))

    def __make_elements(proto_elements:List[ProtoBase]]):
        syntax = ''
        for proto_element in self.proto_elements:
            syntax += proto_element.make()
        return syntax

    def add_message(self, message:ProtoMessage):
        self.__messages.append(message)

    def make(self):
        fields = self.__make_elements(self.__fields)
        messages = self.__make_messages(self.__messages)
        return MESSAGE_FORMAT.format(fields, messages)
