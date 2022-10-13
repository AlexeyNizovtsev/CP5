a=[1,2,3,4,5]
mini=min(a)
delta= 4
cnt=0

for i in a:
    if i-delta==mini:
        cnt+=1
print(cnt)