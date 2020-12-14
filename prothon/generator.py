import openpyxl
from prothon.proto_message import ProtoMessage
from prothon.proto_const import ROOT_HIERARCHY_NAME


def __is_excel_file(file_name):
    if '$' in file_name or '.meta' in file_name:
        print('[prothon] Not exceel file ' + file_name)
        return False
    return True


def __format_proto(proto):
    open_bracket = '{'
    close_bracket = '}'
    indent = '\t'

    # Formatting
    formatted = ''
    proto = proto.replace('message ', '\nmessage ')
    proto = proto.replace(open_bracket, '\n{\n')
    proto = proto.replace(close_bracket, '}\n\n')
    proto = proto.replace(';', ';\n')
    proto = proto.replace('}\n\n}', '}\n}')

    indent_level = 0
    for line in proto.splitlines():

        if close_bracket in line:
            indent_level -= 1

        indents = indent * indent_level
        formatted += indents + line + '\n'

        if open_bracket in line:
            indent_level += 1

    return formatted


def generate(excel_path):
    if __is_excel_file(excel_path) is False:
        pass

    proto = 'syntax = "proto3";\n'

    workbook = openpyxl.load_workbook(excel_path)

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
