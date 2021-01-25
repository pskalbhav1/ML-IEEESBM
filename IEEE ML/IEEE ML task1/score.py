#Q.5 score
n=int(input())
l1=[]
for i in range(n):
    x=int(input())
    l1.append(x)
l1.sort()
print(l1[n-2])

