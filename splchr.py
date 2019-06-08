a=input()
c=0
b=0
for i in range(len(a)):
    if(a[i].isalpha() or a[i].isdigit()):
        b=b+1
    else:
        c=c+1
print(c)
