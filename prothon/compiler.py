import os
import platform
import subprocess
from prothon.proto_const import COMPILE_OPTION_MAP


def __is_proto_file(file_name):
    if '$' in file_name or '.meta' in file_name:
        print('[ProtoCompiler] Not proto file ' + file_name)
        return False

    return file_name.endswith('.proto')

def __get_compiler_name():
    return 'protoc.exe' if platform.system() == 'Windows' else 'protoc'

def __compile_proto(proto_path, import_path, out_option, dest_path):

    # Linux: Linux
    # Mac: Darwin
    # Windows: Windows
    compiler_path = os.path.abspath(f'./prothon/compiler/{__get_compiler_name()}')
    command = f'{compiler_path} -I={import_path} --{out_option}={dest_path} {proto_path}'
    subprocess.call(command)


# protoc -I=$SRC_DIR --csharp_out=$DST_DIR $SRC_DIR/addressbook.proto
def compile(proto_path, import_path, target_language, dest_path):
    """Compile .proto file to code

    :import_path : Import otehr proto file path
    :target_language : Output option
    :proto_path : Proto file path
    :dest_path : Output destination path
    """
    if __is_proto_file(proto_path) is False:
        pass

    if target_language not in COMPILE_OPTION_MAP:
        print('[ProtoCompiler] Not availiable language : ' + target_language)
        pass

    out_option = COMPILE_OPTION_MAP[target_language]
    __compile_proto(proto_path, import_path, out_option, dest_path)
