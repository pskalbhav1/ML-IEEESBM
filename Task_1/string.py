l1 =(input("\nEnter the stings : \n ").split())
l2=["1","5","e"]
cnt2=0
for i in l1:
    if len(i)>=4:
        cnt=0
        for j in l2:
            if (i[0]==j or i[len(i)-1]==j):
                cnt+=1
        if cnt==0:
            cnt2+=1
print(l1)
print(cnt2)

