import pandas as pd
def opt5():
    df = pd.read_csv('rc.csv',delimiter=',')
    length=len(df.index)
    if length==0:
        print('No data')
        return
    heading=['Name','Admission Number','Roll Number','Class',
    'Science','Maths','Social Studies','English']
    l=len(df.index)
    per=[]
    #creating empty dataframe
    a = pd.DataFrame(columns=heading)
    #if all marks of a student are >90 append their details to dataframe 'a'
    #calculate the percentage of merit students and make a list of them
    for i in range(l):
        if df.iloc[i]['Science']>90 and df.iloc[i]['Maths']>90 and df.iloc[i]['Social Studies']>90 and df.iloc[i]['English']>90:
            a=a.append(df.loc[i],ignore_index=True)
            tmark = df.iloc[i]['Science']+df.iloc[i]['Maths']+df.iloc[i]['Social Studies']+df.iloc[i]['English']
            perc = (tmark*100)/400
            perc = round(perc,2)
            per.append(perc)
    if a.empty:
        print('No merit student')
        return
    #add new column of percentage list to dataframe 'a'
    a['Percentage']=per

    print(a)
