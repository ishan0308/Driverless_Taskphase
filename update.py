import pandas as pd
def opt2():
    df = pd.read_csv('rc.csv',delimiter=',')
    length=len(df.index)
    if length==0:
        print('No data')
        return
    df = pd.read_csv('rc.csv',delimiter=',',header=None)
    print(df)
    #input row index to know which student's detail are to be updated
    if length>1:
        line = 'Enter row index(1-'+str(length)+') : '
        s=input(line)
        while s.isdigit() is False or int(s) not in range(1,length+1):
            print('Incorrect')
            s=input(line)
    else: s=1
    idx=int(s)-1
    #take column input to know which info is to be updated
    col=input('Enter column index(0-7) : ')
    headings=['0','1','2','3','4','5','6','7']
    while col not in headings:
        print('Incorrect')
        col=input('Enter column index(0-7) : ')
    #input the new info
    if col=='0':
        heading='Name'
        new=input('New Full Name : ')
        dig=any(chr.isdigit() for chr in new)
        while dig:
            print('Incorrect')
            new=input('New Full Name : ')
            dig=any(chr.isdigit() for chr in new)
        new=new.title()
    elif col=='1':
        heading='Admission Number'
        s=input('New Admission number(4 digit) : ')
        while len(s)!=4 or s.isdigit() is False:
            print('Incorrect')
            s=input('New Admission number(4 digit) : ')
        new=int(s)

    elif col=='2':
        heading='Roll Number'
        s=input('New Roll number : ')
        while s.isdigit() is False:
            print('Incorrect')
            s=input('New Roll number : ')
        new=int(s)

    elif col=='3':
        heading='Class'
        s=input('New Class(1-12) : ')
        while s.isdigit() is False or int(s) not in range(1,13):
            print('Incorrect')
            s=input('New Class(1-12) : ')
        new=int(s)

    else:
        if col=='4':
            heading='Science'
            sub="New Science marks(out of 100) :"
        elif col=='5':
            heading='Maths'
            sub="New Maths marks(out of 100) :"
        elif col=='6':
            heading='Social Studies'
            sub="New Social Studies marks(out of 100) :"
        else:
            heading='English'
            sub="New English marks(out of 100) :"

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
        new=float(s)

    df = pd.read_csv('rc.csv')
    #update
    df.at[idx,heading]=new
    df.to_csv('rc.csv',index=False)
    df = pd.read_csv('rc.csv',delimiter=',',header=None)
