import json

json_str = '[{"name":"jchen","age":18},{"name":"jchen","age":18}]'

student = json.loads(json_str)

print(type(student))
print(student)