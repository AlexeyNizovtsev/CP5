from random import randint

s=int(input('Размерность массивов: '))
a=[0]*s
b=[0]*s
for i in range(s):
    a[i]= randint(1, 10)
    b[i]= randint(1, 10)

print(a)
print(b)
dub=[]
for i in a:
    for j in b:
        if i==j and i not in dub:
            dub.append(i)
print(*dub)
    
    