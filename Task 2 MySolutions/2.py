import numpy as np

ar=np.array([('James',5,48.5),('Nail',6,52.5),('Paul',5,42.1),('Pit',5,40.11)])

# sorting array based on class
for x in range(0,len(ar)):
    index=x
    smallclass=ar[x][1]
    smallname=ar[x][0]
    smallheight=ar[x][2]
    for y in range(x+1,len(ar)):
        if ar[y][1]<smallclass:
            smallclass=ar[y][1]
            smallname=ar[y][0]
            smallheight=ar[y][2]
            index=y
    t=ar[x][1]
    ar[x][1]=smallclass
    ar[index][1]=t
    t=ar[x][0]
    ar[x][0]=smallname
    ar[index][0]=t
    t=ar[x][2]
    ar[x][2]=smallheight
    ar[index][2]=t

# sorting array based on height if and only if class is equal
for x in range(0,len(ar)):
    index=x
    smallclass=ar[x][1]
    smallname=ar[x][0]
    smallheight=ar[x][2]
    for y in range(x+1,len(ar)):
        if ar[x][1]!=ar[y][1]: break
        if ar[y][2]<smallheight:
            smallclass=ar[y][1]
            smallname=ar[y][0]
            smallheight=ar[y][2]
            index=y
    t=ar[x][1]
    ar[x][1]=smallclass
    ar[index][1]=t
    t=ar[x][0]
    ar[x][0]=smallname
    ar[index][0]=t
    t=ar[x][2]
    ar[x][2]=smallheight
    ar[index][2]=t


print(ar)