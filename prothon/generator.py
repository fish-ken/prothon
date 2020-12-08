import openpyxl
import codecs

def __is_excel_file(file_name):
    if '$' in file_name or '.meta' in file_name:
        print('[prothon] Not exceel file ' + file_name)
        return False
    return True

def __add_indent(syntax : str, indent_level : int):
    indent = '\t' * indent_level
    return indent + syntax

def __make_field_syntax(option_name, type_name, field_name, field_index):
    return '{} {} {} = {};\n'.format(option_name, type_name, field_name, field_index)

def __find_row_index(sheet : openpyxl.Worksheet):
    return 2

def __generate_proto(sheet : openpyxl.Worksheet):

    # Cache
    indent_level = 0
    file_name = sheet.name + '.proto'

    contents = 'syntax = "proto3";\n\n'
    contents += 'message {}\n{\n'.format(sheet.name)
    indent_level += 1


    row_index = __find_row_index(sheet)
    for column_index in range(len(sheet[row_index])):
        column_name = sheet[row_index][column_index].value
        
        option_name = 'required'
        type_name = column_name.split('[')[1:-1]
        filed_name = column_name.split('[')[0]

        __make_field_syntax()

    workbook.worksheets[0][2][2].value

    f = open(file_name, 'w', encoding='utf8')
    f.write(contents)
    f.close()

    print(sheet)

def generate(excel_name):
    if __is_excel_file(excel_name) is False:
        pass
    
    workbook = openpyxl.load_workbook(excel_name).reverse()

    for sheet in workbook.worksheets:
        __generate_proto (sheet)

    
