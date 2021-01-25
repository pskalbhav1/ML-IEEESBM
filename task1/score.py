num=int(input("enter how many scores you want to insert\n"))
list=[]
for i in range(0,num):
    x = int(input("enter no\n"))
    list.append(x)
print(list)

#now to find second last no
l2=[]
for i in list:
    if i not in l2:
        l2.append(i)
l2.sort()
print(l2[-2])
