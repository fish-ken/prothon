import prothon
from glob import glob 

EXCEL_PATH = './Excel/'
EXPORT_PROTO_PATH = './Proto/'


# Return *.proto files name
def get_proto_list():
    pattern = EXPORT_PROTO_PATH + '**[!*.meta]'
    return glob(pattern)


# Compile *.proto
def compile_proto(excel_path):
    prothon.compile(excel_path)


if __name__ is '__main__':
    for name in get_proto_list():
        compile_proto(name)
        break





