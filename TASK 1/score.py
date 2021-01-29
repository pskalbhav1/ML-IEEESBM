List1=[]

n = int(input("Enter number of elements in list: "))
        
scores=[] 

for i in range(0, n): 
    ele = int(input())

scores.append(ele)
        
List1.sort()

print("runner up is:",List1[-2])
 
