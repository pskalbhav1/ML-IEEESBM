#Q.10 string
l1=[]
n=int(input("Enter the length of the list:"))
for i in range(n):
    x=input("Enter the string:")
    l1.append(x)
count=0
for j in (l1):
    if (len(j)>3 and j[0]!=j[-1]):
        count=count+1
print(count)
