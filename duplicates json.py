import json
x='{"a":  1,"a":  2,"a":  3,"a": 4,"b": 1, "b": 2}'
y=json.loads(x)
print(y)



x={"a":  1,"a":  2,"a":  3,"a": 4,"b": 1, "b": 2}
with open("dump.json","w") as file:
    data=json.dump(x,file,indent=4)
    