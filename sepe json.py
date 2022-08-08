import json
dic={}
with open("sepe.txt") as f:
    for i in f:
        key,desc=i.strip().split()
        dic[key]=desc.strip
        
        
        # print(i)
        # print(a[i])
    
        # b=desc.strip()
        # print(dic)
with open("sep dump.json","w") as s:
    json.dump(dic,s,indent=6)