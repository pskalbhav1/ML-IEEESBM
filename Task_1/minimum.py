l1 = list(map(int,input("\nEnter 5 numbers or more : \n ").split())) 
l1=list(dict.fromkeys(l1))
l1.sort()
print(l1[2])
