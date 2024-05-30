# [prothon](https://pypi.org/project/prothon/)
Generate/Compile proto files  


## Installation
```bash
pip install prothon
```

## Quickstart
```python
import prothon


def generate_example():
    excel_path = 'YOUR EXCEL PATH'
    proto_name = 'YourProto.proto'

    proto = prothon.generate(excel_path)

    f = open(proto_name, 'w', encoding='utf8')
    f.write(proto)
    f.close()


def compile_example():
    # Your target language
    language = 'csharp'                     
    proto_path = 'YOUR PROTO FILE PATH'
    prothon.compile(proto_path, './', language, './')
```
