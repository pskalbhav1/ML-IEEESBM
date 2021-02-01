n=int(input("Enter the no. of Scores\n"))
l1 = list(map(int,input("\nEnter the Scores : \n ").split())) 
l1.sort()
for i in range(n-1,0,-1):
    if l1[i-1]<l1[i]:
        print(l1[i-1])
        break