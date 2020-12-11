

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
        print('[ProtoGenerator] Not exceel file ' + file_name)
        return False
    return True

# Compile *.proto


def __compile_proto(sheet):
    print(sheet)


def compile(proto_name):
    if __is_proto_file(proto_name) is False:
        pass

    __compile_proto(proto_name)
