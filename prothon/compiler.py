#import platform
import subprocess

compile_option_map = {
    'csharp': 'csharp_out',
    'cpp': 'cpp_output',
    'python': 'python_out',
    'java': 'java_out',
    'go': 'go_out',
    'dart': 'dart_out',
}


def __is_proto_file(file_name):
    if '$' in file_name or '.meta' in file_name:
        print('[ProtoCompiler] Not proto file ' + file_name)
        return False

    return file_name.endswith('.proto')


def __compile_proto(proto_path, import_path, out_option, dest_path):
    command = 'compiler/protoc.exe -I={0} --{1}={2} {3}'.format(
        import_path, out_option, dest_path, proto_path)
    subprocess.call(command, shell=False)


# protoc -I=$SRC_DIR --csharp_out=$DST_DIR $SRC_DIR/addressbook.proto
def compile(proto_path, import_path, target_language, dest_path):
    """
    :import_path : Import otehr proto file path
    :target_language : Output option
    :proto_path : Proto file path
    :dest_path : Output destination path
    """
    if __is_proto_file(proto_path) is False:
        pass

    if target_language not in compile_option_map:
        print('[ProtoCompiler] Not availiable language : ' + target_language)
        pass

    out_option = compile_option_map[target_language]
    __compile_proto(proto_path, import_path, out_option, dest_path)
