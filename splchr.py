a=str(input())
c=0

for i in range(len(a)):
    if(a[i].isalpha()!=1):
        if(a[i]!=" "):
           c=c+1
print(c)
