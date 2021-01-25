l1 =[20, 67, 385 ,165 , 52, 33, -19 , 0 , -220 , -66]
l2=list()
for i in l1:
    if i%55==0:
        l2.append(i)


for j in l1:
    if j%33==0:
        l2.append(j)
#remove common elements

l3=list()
for k in l2:
    if k not in l3:
        l3.append(k)

print(l3)
