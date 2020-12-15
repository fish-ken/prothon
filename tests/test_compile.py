import os
import prothon
from prothon.compiler import compile_option_map
from glob import glob

PROTO_PATH = './proto/'


def __get_proto_list():
    pattern = PROTO_PATH + '[!~$]**[!*.meta]'
    return glob(pattern)


def __remove_compile_output():
    compile_output = glob('./compile_output')
    for path in compile_output:
        os.remove(path)


def test_compile():
    __remove_compile_output()

    for proto_path in __get_proto_list():
        for language in compile_option_map.keys():
            prothon.compile(proto_path, './proto/',
                            language, './compile_output/')

    print(glob(PROTO_PATH))
