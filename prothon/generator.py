import openpyxl
from prothon.proto_message import ProtoMessage


def __is_excel_file(file_name):
    if '$' in file_name or '.meta' in file_name:
        print('[prothon] Not exceel file ' + file_name)
        return False
    return True

# def __add_indent(syntax: str, indent_level: int):
#     indent = '\t' * indent_level
#     return indent + syntax


def generate(excel_name):
    if __is_excel_file(excel_name) is False:
        pass

    proto = 'syntax = "proto3";\n\n'

    workbook = openpyxl.load_workbook(excel_name)

    for sheet in workbook.worksheets:
        message = ProtoMessage(sheet)

        # TODO : Make hierarchy

        return proto + message.make()

    # TODO : Validate hierarchy


