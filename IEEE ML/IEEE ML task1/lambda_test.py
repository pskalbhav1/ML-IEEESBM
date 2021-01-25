#Q.6 lambda_test
l1=[]
n=int(input("Enter the length of the list "))
for i in range(n):
    x=int(input("Enter the element "))
    l1.append(x)
print("The list created is ",l1)
for j in(l1):
    if(j%33==0 or j%55==0):
        print(j,end="  ")
