def f1(d, v):
    list=[]
    
    for key in d:
        if str(d.get(key)) == v:
            list.append(key)
    if list==[]:
        return "No Key"
    return list
d = {
  "stu":"Lisa",
  "n":19,
  "brand": "qw",
  "model": "98HW",
  "year": 19
}
a = input()
print(f1(d,a))