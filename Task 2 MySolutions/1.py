import numpy as np

ar1=np.array([1023,5202,6230,1671,1682,5241,4532])
ar2=ar1.copy()
l=len(ar2)

# sorting array ar2
for x in range(0,l):
    index=x
    small=ar2[x]
    for y in range(x+1,l):
        if ar2[y]<small:
            small=ar2[y]
            index=y
        y+=1
    t=ar2[x]
    ar2[x]=small
    ar2[index]=t
    x=x+1

# filling ar_indices with indices of sorted array by comparing ar2 and ar1
ar_indices=ar1.copy()
for x in range(0,l):
    for y in range(0,l):
        if(ar1[x]==ar2[y]):
            ar_indices[x]=y
            break
        y+=1
    x+=1

print(ar1)
print(ar2)
print(ar_indices)