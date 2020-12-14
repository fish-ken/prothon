import openpyxl
from prothon.proto_message import ProtoMessage
from prothon.proto_const import ROOT_HIERARCHY_NAME

def __is_excel_file(file_name):
    if '$' in file_name or '.meta' in file_name:
        print('[prothon] Not exceel file ' + file_name)
        return False
    return True

# def __add_indent(syntax: str, indent_level: int):
#     indent = '\t' * indent_level
#     return indent + syntax


def __format_proto(proto):
    formatted = proto
    formatted = formatted.replace('message ', '\nmessage ')
    formatted = formatted.replace('{', '\n{\n')
    formatted = formatted.replace('}', '}\n\n')
    formatted = formatted.replace(';', ';\n')
    formatted = formatted.replace('}\n\n}', '}\n}')

    # for character in proto:
    #     print(character)

    return formatted



def generate(excel_name):
    if __is_excel_file(excel_name) is False:
        pass

    proto = 'syntax = "proto3";\n'

    workbook = openpyxl.load_workbook(excel_name)

    message_map = {}

    # Construct message   
    for sheet in workbook.worksheets:
        message = ProtoMessage(sheet)
        message_map[message.name] = message

    # Make hierarchy
    message_root_name = None
    for message in message_map.values():
        if message.parent == ROOT_HIERARCHY_NAME:
            message_root_name = message.name
            continue

        message_map[message.parent].add_message(message)
        
    # Return proto string


    return proto + __format_proto(message_map[message_root_name].make())


