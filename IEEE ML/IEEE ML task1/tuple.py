# Q.1  tuple
t1 = ()
n = int(input("Enter the length : "))
for i in range(n):
    x = input("Enter the element")
    t1 = t1+(x,)
print("The tuple is ",t1)
print("The third element is ",t1[2])
print("The second last element is ",t1[n-2])


