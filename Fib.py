summ = 1
nm=0
x=1
y=0
while nm<4000000:
    x=y
    y=summ
    summ= x+y
    if summ % 2==0:
     nm+=summ
print(int(nm))
     