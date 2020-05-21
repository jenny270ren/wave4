a = input()
b = a.split()
y=0
x=0
for x in b:
    c = b[y]
    if c[0]=="a" or c[0]=="e" or c[0]=="i" or c[0]=="o" or c[0]=="u":
        print(c+"way ", end ='')
    else:
        while c[0]!="a" and c[0]!="e" and c[0]!="i" and c[0]!="o" and c[0]!="u":
            c = c+c[0]
            c = c[1:]
        print (c+"ay ", end ='')
    y+=1
