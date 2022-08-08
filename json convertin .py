a={"shopping_list":{"chaco":"15","Biscuits":"50","Diary_milk":"30","ice_cream":"20",}}
b= input("enter the what you want ")
h=int(input("enter how many you want"))
import json
for i in a:
    # print(a[i][b])
    if a[i][b]==a[i][b]:
        c=a[i][b]
        s=int(c)
        # print(s-h)
        d={}
        dic={}
        n=s-h
        # print(n)
    for key in a:
        for value in a[key]:
            # print(value)
            d[value]=a[key][value]
            if value==b:
                d[value]=n
                dic[key]=d
out_file = open("sushfile.json", "w")
json.dump(dic, out_file, indent = 6)
out_file.close()
