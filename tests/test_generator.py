import os
from glob import glob
import prothon

EXCEL_PATH = './excel/'
EXPORT_PROTO_PATH = './proto/'


def __get_excel_list():
    pattern = EXCEL_PATH + '[!~$]**[!*.meta]'
    return glob(pattern)


# Return *.xlsx files name
def test_generate():
    for excel_path in __get_excel_list():
        name = os.path.basename(excel_path).split('.')[0]
        cache_proto = open(EXPORT_PROTO_PATH + name,
                           'r', encoding='utf8').read()
        gen_proto = prothon.generate(excel_path)
        assert gen_proto == cache_proto
