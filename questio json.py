import json
name=input("enter the number")
age=int(input("enter the number"))
dic={"name":name,"age":age}
with open("question op.json","w") as f:
    json.dump(dic,f,indent=4)
