from typing import List
import openpyxl
from openpyxl.utils import get_column_letter

from prothon.proto_base import ProtoBase
from prothon.proto_field import ProtoField
from prothon.proto_enum import ProtoEnum
from openpyxl.utils import get_column_letter

ROOT_HIERARCHY_NAME = 'root'
HIERARCHY_ROW_INDEX = 1
COLUMN_ROW_INDEX = 2

HIERARCHY_IDENTIFIER = '*'
IGNORE_COLUMN_IDENTIFIER = '~'

MESSAGE_FORMAT = \
    'message {0}\n\
{{\
\n\
{1}\
\n\
{2}\
\n\
{3}\
\n\
}}'


class ProtoMessage(ProtoBase):
    """Protobuf message type class

    :param sheet : excel worksheet
    """

    @property
    def parent(self):
        return self.__parent

    @property
    def name(self):
        return self.__name

    def __init__(self, sheet: openpyxl.worksheet):
        self.__sheet = sheet
        self.__parent = ''
        self.__name = self.__sheet.title
        self.__enums = []
        self.__fields = []
        self.__messages = []
        self.__field_index = 0
        self.__initialize()

    def __initialize(self):
        self.__parent = self.__sheet[HIERARCHY_ROW_INDEX][0].value[1:]

        for column_index in range(len(self.__sheet[COLUMN_ROW_INDEX])):
            column_name = self.__sheet[COLUMN_ROW_INDEX][column_index].value

            if column_name is None:
                continue

            if IGNORE_COLUMN_IDENTIFIER in column_name:
                continue

            if HIERARCHY_IDENTIFIER in column_name:
                continue

            column_elements = column_name.split('[')

            # Field declaration
            option = None       # TODO : Variable option
            type_name = column_elements[1][:-1]
            name = column_elements[0]
            self.__field_index += 1
            self.__fields.append(ProtoField(
                option, type_name, name, self.__field_index))

            # Enum declaration
            if type_name == 'enum':
                column_header = self.__sheet[COLUMN_ROW_INDEX][column_index].column
                enum = ProtoEnum(self.__sheet, column_header, name)
                self.__enums.append(enum)


    def __make_elements(self, proto_elements: List[ProtoBase]):
        syntax = ''
        for proto_element in proto_elements:
            syntax += proto_element.make()
        return syntax

    def add_message(self, message):
        # Add message declaration
        self.__messages.append(message)

        # Add message as repeated field
        field_name = message.name[0].lower() + message.name[1:]
        self.__field_index += 1
        self.__fields.append(ProtoField(
            'repeated', message.name, field_name, self.__field_index))

    def make(self):
        enums = self.__make_elements(self.__enums)
        fields = self.__make_elements(self.__fields)
        messages = self.__make_elements(self.__messages)
        return MESSAGE_FORMAT.format(self.__name, enums, fields, messages)
