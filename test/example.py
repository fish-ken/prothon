import prothon
from glob import glob 

EXCEL_PATH = './Excel/'
EXPORT_PROTO_PATH = './Proto/'

# Return *.xlsx files name
def get_excel_list():
    pattern = EXCEL_PATH + '[!~$]**[!*.meta]'
    return glob(pattern)

# Return *.proto files name
def get_proto_list():
    pattern = EXPORT_PROTO_PATH + '**[!*.meta]'
    return glob(pattern)

# Generate *.proto by *.xlsx
def generate_proto(excel_path):
    prothon.generate(excel_path)

# Compile *.proto
# def compile_proto(proto_name):
#     pass


if __name__ is '__main__':

    for name in get_excel_list():
        generate_proto(name)
        break

    # for name in get_proto_list():
    #     compile_proto(name)




