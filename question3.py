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
    print("is not palindrome")
    str=""
    for c in lis:
        str+=c
    for i in range(l+1):#first half
        for n in range(l-i): #for the spaces
            print(" ",end="")
        print(str[0:i+1],end="")
        str2=""
        print(str2.join(reversed(str[0:i])))
    for i in reversed(range(l)):#second half
        for n in range(l-i): #for spaces
            print(" ",end="")
        print(str[0:i+1],end="")
        str2=""
        print(str2.join(reversed(str[0:i])))
    print()
else:
    print("is palindrome")
    for c in lis:
        s = hex(int(ord(c)))
        print(s[2:],end=" ")
