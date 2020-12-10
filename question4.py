file1 = open('names.csv')
d = dict()
#creating dict from csv
# name as value and no. as key
for line in file1:
    x=line.rstrip().split(',')
    d[x[1]]=x[0]

sort = sorted(d.items())
file1.close()
#rewrite the sorted csv file
file = open('names.csv',"w")
for k,v in sort:
    file.write(v+","+k+"\n")
file.close()
# prsint sorted csv file
file4 = open('names.csv',"r")
for line in file4:
    print(line,end="")
file4.close()
#eliminate odd rows
file2 = open('names.csv',"w")
c = 0
for k,v in sort:
    c = c+1
    if c%2==0:
        file2.write(v+","+k+"\n")
print()
file2.close()
#print modified file
#create string of names
file3 = open('names.csv',"r")
s = ""
for line in file3:
    print(line,end="")
    a = line.rstrip().split(',')
    s = s+a[0]

#find min non zero absolute diff btw characters
n = len(s)
m = 10**20
print()
print(s)
for i in range(n-1):
    for j in range(i+1,n):
        x = abs(int(ord(s[i]))-int(ord(s[j])))
        if x<m and x!=0:
            m=abs(int(ord(s[i]))-int(ord(s[j])))

print("minimum difference :",m)
