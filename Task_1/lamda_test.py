l1 = list(map(int,input("\nEnter the numbers : ").split())) 
x= list(filter(lambda num: num%33==0 or num%55==0,l1))
print (x)

