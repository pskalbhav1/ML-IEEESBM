l=[]

# Making sure min of 5 Entries is provided by user
while len(l)<5:
    l=[int(x) for x in input().split()]
    if len(l)<5:
        print("Enter atleast 5 numbers")

# removing duplicate entries if any
l=list(dict.fromkeys(l))

# sorting in ascending order
l.sort()

# printing 3rd least number
print(l[2])

