a=str(input())
c=0
for i in range(len(a)):
    if(a[i].isnumeric()):
        c=c+1
print(c)
