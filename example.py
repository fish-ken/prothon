import prothon
from glob import glob

EXCEL_PATH = './tests/Excel/'
EXPORT_PROTO_PATH = './Proto/'


# Return *.xlsx files name
def get_excel_list():
    pattern = EXCEL_PATH + '[!~$]**[!*.meta]'
    return glob(pattern)


# Generate *.proto by *.xlsx
def generate_proto(excel_path):
    prothon.generate(excel_path)


if __name__ == '__main__':
    for name in get_excel_list():
        generate_proto(name)
