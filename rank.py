import pandas as pd
def opt4():
    df = pd.read_csv('rc.csv',delimiter=',')
    #copying the dataframe
    df2=df
    length=len(df.index)
    if length==0:
        print('No data')
        return
    l=len(df.index)
    x = input('How many ranks : ')
    if x.isdigit() is False or int(x)>l:
        print('Wrong Entry')
        return
    num=int(x)
    percentage=[]
    #calculating percentages of each student and appending it to a list
    for i in range(l):
        tmark = df.iloc[i]['Science']+df.iloc[i]['Maths']+df.iloc[i]['Social Studies']+df.iloc[i]['Maths']
        perc = (tmark*100)/400
        perc = round(perc,2)
        percentage.append(perc)
    #adding a percentage column to dataframe
    df2['Percentage']=percentage
    #sorting dataframe in descending order based on percentage
    df2.sort_values("Percentage", axis = 0, ascending = False,inplace = True, na_position ='last')
    print(df2.head(num).to_string(index=False))
