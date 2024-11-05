l=[1,2,3,4,5,"a",2.3]
print(l[0])
print(l[-1])
for i in l:
    print(i)
l.insert(6,"b")
print(l)
l.append(True)
print(l)
l[2]=12
print(l)
del l[0]
print(l)
#Tuple
val=(1,2,"a",2.5,True)
print(val[1])

#Dictionary
d={"a":2, 4:"hello", "world":"good morning"}
print(d[4])
print(d["world"])

d2={}
d2["firstname"]="Pratik"
d2["lastname"]="sengupta"
print(d2)
