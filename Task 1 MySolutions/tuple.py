n=int(input("Enter number of elements of tuple = "))
i=0
l=[]
print("Enter elements of tuple")
while i<n:
    l.append(input())
    i+=1
t=tuple(l)

# printing 3rd element
print("\n3rd element is ",t[2])
# printing 2nd last element
print("2nd last element is ",t[-2])
