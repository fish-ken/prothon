# prothon
Generate .proto by .xlsx 
> Based on proto3

## Installation
```
some installation
```

## Quick start
```py
import prothon

excel_path = 'YOUR EXCEL PATH'
proto_name = 'YourProto.proto'

proto = generate_proto(excel_path)

f = open(proto_name, 'w', encoding='utf8')
f.write(proto)
f.close()
```
