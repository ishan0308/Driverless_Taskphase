import pandas as pd
def opt3():
    df = pd.read_csv('rc.csv',delimiter=',')
    length=len(df.index)
    if length==0:
        print('No data')
        return
    s = input('Display by Class/Roll Number/Name - ')
    s=s.title()
    while s!='Name' and s!='Class' and s!='Roll Number':
        print('Incorrect')
        s = input('Display by Class/Roll Number/Name - ')
        s=s.title()

    report = pd.read_csv('rc.csv',delimiter=',')
    #input class/roll no./name and print the row of dataframe having that input
    if s=='Class':
        n=input('Class(1-12) : ')
        while n.isdigit() is False or int(n) not in range(1,13):
            print('Incorrect')
            n=input('Class(1-12) : ')
        c=int(n)
        rt=report.loc[report['Class']==c]
        if rt.empty:
            print('Class does not exist')
            return
        print(rt)

    elif s=='Roll Number':
        n=input('Roll number : ')
        while n.isdigit() is False:
            print('Incorrect')
            n=input('Roll number : ')
        r=int(n)
        rt=report.loc[report['Roll Number']==r]
        if rt.empty:
            print('Roll Number does not exist')
            return
        print(rt)

    else:
        n=input('Full Name : ')
        dig=any(chr.isdigit() for chr in n)
        while dig:
            print('Incorrect')
            n=input('Full Name : ')
            dig=any(chr.isdigit() for chr in n)
        rt=report.loc[report['Name']==n]
        if rt.empty:
            print('Name does not exist')
            return
        print(rt)
