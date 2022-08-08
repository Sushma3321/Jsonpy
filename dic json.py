# import json
# student='{"name":"sachin","age":45,"db":"4th march"}'
# st=json.loads(student)
# print(st)


import json
with open("load.json","r") as file:
    data=json.load(file)
    print(data)