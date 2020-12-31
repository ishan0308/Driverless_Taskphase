def opt1():
    detail=[]
    for i in range(8):
        if i==0:
            n=input('Full Name : ')
            dig=any(chr.isdigit() for chr in n)
            while dig:
                print('Incorrect')
                n=input('Full Name : ')
                dig=any(chr.isdigit() for chr in n)
            n=n.title()
            detail.append(n)

        elif i==1:
            s=input('Admission number(4 digit) : ')
            while len(s)!=4 or s.isdigit() is False:
                print('Incorrect')
                s=input('Admission number(4 digit) : ')
            a=int(s)
            detail.append(a)

        elif i==2:
            s=input('Roll number : ')
            while s.isdigit() is False:
                print('Incorrect')
                s=input('Roll number : ')
            r=int(s)
            detail.append(r)

        elif i==3:
            s=input('Class(1-12) : ')
            while s.isdigit() is False or int(s) not in range(1,13):
                print('Incorrect')
                s=input('Class(1-12) : ')
            c=int(s)
            detail.append(c)

        else:
            if i==4:sub="Science marks(out of 100) :"
            elif i==5:sub="Maths marks(out of 100) :"
            elif i==6:sub="Social Studies marks(out of 100) :"
            else:sub="English marks(out of 100) :"

            while True:
                s=input(sub)
                try :
                    float(s)
                except :
                    print("Incorrect")
                    continue
                if not 0<= float(s) <=100:
                    print('Incorrect')
                    continue
                break
            m=float(s)
            detail.append(m)
    return detail
