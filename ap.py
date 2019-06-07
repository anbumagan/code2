n,a,d=input().split()
X=int(n)
Y=int(a)
Z=int(d)
total = (X * (2 * Y + (X - 1) * Z)) / 2
print(int(total))
