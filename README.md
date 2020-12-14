# prothon
Generate .proto by .xlsx.  
Compile .proto

## Installation
```bash
pip install prothon
```

## Quick start
```python
import prothon

excel_path = 'YOUR EXCEL PATH'
proto_name = 'YourProto.proto'

proto = generate_proto(excel_path)

f = open(proto_name, 'w', encoding='utf8')
f.write(proto)
f.close()
```
