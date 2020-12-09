import prothon
import os
from glob import glob


EXCEL_PATH = './tests/Excel/'
EXPORT_PROTO_PATH = './Proto/'


# Return *.xlsx files name
def get_excel_list():
    pattern = EXCEL_PATH + '[!~$]**[!*.meta]'
    return glob(pattern)


# Generate *.proto by *.xlsx
def generate_proto(excel_path):
    return prothon.generate(excel_path)


if __name__ == '__main__':
    for excel_name in get_excel_list():
        proto = generate_proto(excel_name)
        proto_name = os.path.basename(excel_name).split('.')[0] + '.proto'

        f = open(proto_name, 'w', encoding='utf8')
        f.write(proto)
        f.close()
