import openpyxl
import codecs

def __is_excel_file(file_name):
    if '$' in file_name or '.meta' in file_name:
        print('[prothon] Not exceel file ' + file_name)
        return False
    return True

def __generate_proto(sheet):
    print(sheet)

def generate(excel_name):
    if __is_excel_file(excel_name) is False:
        pass
    
    workbook = openpyxl.load_workbook(excel_name)

    for sheet in workbook.worksheets:
        __generate_proto (sheet)

    
