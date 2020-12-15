import prothon
import os
from glob import glob


EXCEL_PATH = './tests/excel/'
EXPORT_PROTO_PATH = './tests/proto/'


def get_excel_list():
    """
    Return *.xlsx files name
    """
    pattern = EXCEL_PATH + '[!~$]**[!*.meta]'
    return glob(pattern)


def get_proto_list():
    """
    Return *.proto files name
    """
    pattern = EXPORT_PROTO_PATH + '[!~$]**[!*.meta]'
    return glob(pattern)


if __name__ == '__main__':

    # Generate example
    for excep_path in get_excel_list():
        proto = prothon.generate(excep_path)
        proto_name = os.path.basename(excep_path).split('.')[0] + '.proto'

        f = open(EXPORT_PROTO_PATH + proto_name, 'w', encoding='utf8')
        f.write(proto)
        f.close()

    # Compile example
    for proto_path in get_proto_list():
        language = 'csharp'
        prothon.compile(proto_path, './', language, './')
