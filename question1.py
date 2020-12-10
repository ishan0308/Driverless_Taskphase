def mult(X,Y):
    m = len(X)
    n = len(X[0])
    p = len(Y)
    q = len(Y[0])
    if n!=p :
        print("cant be multiplied")
        exit()
    R=[]
    for i in range(m):
        r=[]
        for j in range(q):
            c=0
            for k in range(n):
                c+= X[i][k] * Y[k][j]
            r.append(c)
        R.append(r)
    for arr in R:
        print(arr,end="")
        print()
    return R

def trans(X):
    Z=[]
    for j in range(len(X[0])):
        l=[]
        for i in range(len(X)):
            l.append(X[i][j])
        Z.append(l)

    for arr in Z:
        print(arr,end="")
        print()
    return Z

def verify(A,B):
    print("AB : ")
    X = mult(A,B)
    print("LHS :")
    R=trans(X)
    print("TRANSPOSE OF B")
    Y = trans(B)
    print("TRANSPOSE OF A")
    Z = trans(A)
    print("RHS :")
    S=mult(Y,Z)
    if R==S:
        return True
    else:  False

X = [[1, 2, 3],[4, 5, 6],[7, 8, 9]]
Y = [[10,11,12],[13,14,15],[2,3,4]]
if verify(X,Y):
    print("\nLHS = RHS")
    print("Verified")
else:
    print("\nFalse statement")
