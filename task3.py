import pandas as pd
import detail
import update
import marksheet
import rank
import merit
heading=['Name','Admission Number','Roll Number','Class',
'Science','Maths','Social Studies','English']
#add headings if the fle is empty
try:
    header = pd.read_csv('rc.csv',delimiter=',')
except:
    name = pd.DataFrame(columns=heading)
    name.to_csv('rc.csv',index=0)

while True:
    print('===================================')
    print('OPTIONS')
    print('1. Add New Student Detail')
    print('2. Update Stored Detail')
    print('3. Display Marksheet')
    print('4. Compute Ranks')
    print('5. Merit Students')
    print('6. Display complete report card')
    print('7. Exit')
    choice = input('Enter Option Number : ')
    if choice=='1':
        details = detail.opt1()
        stu = pd.DataFrame([details])
        stu.to_csv('rc.csv',mode='a',index=False,header=False)
    elif choice=='2':update.opt2()
    elif choice=='3':marksheet.opt3()
    elif choice=='4':rank.opt4()
    elif choice=='5':merit.opt5()
    elif choice=='6':
        df = pd.read_csv('rc.csv',delimiter=',',header=0)
        length=len(df.index)
        if length==0:
            print('No data')
        else:
            print(df)
    elif choice=='7':
        print('Exiting')
        break
    else:print('Wrong Choice')
