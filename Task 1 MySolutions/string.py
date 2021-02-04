# input
List=input("Enter space separated strings for input\n").split()

count=0
for x in List:
    if len(x)>=4 and x[0]!=x[-1]:
            count+=1

print(count)
