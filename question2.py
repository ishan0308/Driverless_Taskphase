def sumtup(t):
    if len(t)==1:
        return t[0]
    else:
        return t[0]+sumtup(t[1:])

tup = (1,2,4,1,6,2,4,7,4,8)
if tup==():
    print("empty")
    exit()
print(tup)
lis = []
#if number not in the list add to the tuple
for n in tup:
    if n not in lis:
        lis.append(n)

modtup = tuple(lis)
print(modtup)
x=0
s = sumtup(modtup)
print("Sum : ",s)
