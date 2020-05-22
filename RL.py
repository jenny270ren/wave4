def f1(d, v):
    list=[]
    
    for key in d:
        if str(d.get(key)) == v:
            list.append(key)
    if list==[]:
        return "No Key"
    return list

n = int(input("number of items"))
d ={}

for w in range(n):
    k = input("input key name")
    va = input("input value")
    d[k]= va

a = input("enter value to find")
print(f1(d,a))