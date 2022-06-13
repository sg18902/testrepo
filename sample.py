x=(input("write the first string    \n "))
y=(input("write the second string    \n"))
m=len(x)
n=len(y)
lcs=[[0 for i in range(n+1)] for i in range(m+1)]
for i in range(m+1):
    for j in range(n+1):
        if i==0 or  j==0:
            lcs[i][j]=0
        elif(x[i-1]==y[j-1]):
            lcs[i][j]= lcs[i-1][j-1]+1
        else:
            lcs[i][j]=max(lcs[i][j-1] , lcs[i-1][j])

i=m
j=n
l=""
while (i>0 and j>0 ):
    if (x[i-1]==y[j-1]):
        l=x[i-1]+l
        i-=1
        j-=1
    elif lcs[i-1][j]>lcs[i][j-1]:
        i-=1
    else:
        j-=1

print(l)





