import json
d={
    '4': 5, 
    '6': 7, 
    '1': 3, 
    '2': 4}
a=json.dumps(d, sort_keys=True, )
print(a)






