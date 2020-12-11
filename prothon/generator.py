import openpyxl
from prothon.proto_message import *


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

    message_map = {}

    for sheet in workbook.worksheets:
        message = ProtoMessage(sheet)
        message_map[message.name] = message

    # TODO : Make hierarchy    
    for message in message_map.items():
        
        if message.parent == ROOT_HIERARCHY_NAME:
            continue

    return proto + message_map[ROOT_HIERARCHY_NAME].make()


