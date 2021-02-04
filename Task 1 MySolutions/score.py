n=int(input())
l=[]

# Ensuring entries don't exceed input value from user
while len(l)!=n:
    l=[int(x) for x in input().split()]
    if len(l)!=n:
        print("Entries should not exceed ",n)
    else:
        break

l.sort() #Sorting the list

# Finding second biggest number
max=l[-1]
ans=l[0]
i=1
while i<(n-1):
    if(ans<max):
        ans=l[i]
        i+=1
    else:
        break

# Printing The Runner-Up score
print(ans)
