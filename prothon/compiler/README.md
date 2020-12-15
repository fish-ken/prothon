## Complier list
- protoc (for macOS)
- protoc.exe (for Windows 64)

## Usage

```

$SRC_DIR = *.proto directory
$DST_DIR = Exprot directory

# Output
--cpp_out
--csharp_out
--python_out


# cpp example
protoc --cpp_out=$DST_DIR $SRC_DIR/addressbook.proto

# csharp example
protoc --csharp_out=$DST_DIR $SRC_DIR/*.proto
```

