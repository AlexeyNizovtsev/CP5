from random import randint

a=[0]*int(input('Размерность массива: '))
maxn=maxi=0

for i in range(len(a)):
    n=randint(1, 10000)/10
    a[i]=n
    if maxn<n:
        maxi=i
        maxn=n
print(a)

for j in range(maxi+1, len(a)):
    a[j]=0
print(a)
    
    