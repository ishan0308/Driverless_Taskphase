def pal(l):
    if len(l)<1:
        return True
    if l[0]!=l[-1]:
        return False
    return pal(l[1:-1])
    return True

lis = []
while True:
    a = input("Enter char(0 to exit) : ")
    if a=='0':break
    lis.append(a)

l = len(lis)-1
i=0

if pal(lis)==False:
    print("not palindrome")
    for i in range(l+1):#first half
        for n in range(l-i): #for the spaces
            print(" ",end=" ")
        for j in range(0,i+1): #to print from l to r in list
            print(lis[j],end=" ")
        for k in reversed(range(i)):#to print r to l in list
            print(lis[k],end=" ")
        print()
    for i in reversed(range(l)):#second half
        for n in range(l-i): #for spaces
            print(" ",end=" ")
        for j in range(0,i+1): #to print from l to r of list
            print(lis[j],end=" ")
        for k in reversed(range(i)):#to print r to l of list
            print(lis[k],end=" ")
        print()
else:
    print("is palindrome")
    for c in lis:
        s = hex(int(ord(c)))
        print(s[2:],end=" ")
