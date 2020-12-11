from openpyxl.utils import get_column_letter
from prothon.proto_base import ProtoBase
from prothon.proto_const import COLUMN_ROW_INDEX

ENUM_FORMAT = \
    'enum {0}\n\
{{\
\n\
{1}\
\n\
}}'


class ProtoEnum(ProtoBase):
    """
    Proto enum declaration class

    sheet: openpyxl.worksheet
    column_header: column header like 'B'(second column)
    name: enum type name
    """

    def __init__(self, sheet, column_header, name):
        self.__sheet = sheet
        self.__name = name
        self.__column_header = column_header
        self.__enum_elements = ['None']
        self.__initialize()

    def __initialize(self):
        columns = self.__sheet[self.__column_header]

        for i in range(COLUMN_ROW_INDEX, len(columns)):
            value = columns[i].value
            if value in self.__enum_elements:
                continue
            else:
                self.__enum_elements.append(value)

        pass

    def make(self):
        enum_fields = ''

        for i in range(len(self.__enum_elements)):
            field_index = i + 1
            enum_fields += '\t{} = {};\n'.format(
                self.__enum_elements[i], field_index)

        return ENUM_FORMAT.format(self.__name, enum_fields)
