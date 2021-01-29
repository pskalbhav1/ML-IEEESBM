n= int(input("Enter the number of words:"))

words=[n]
count=0
length=0

for j in range(0,n-1):
    words[j]=input("Enter the word:")


for i in range(0,n-1):
    words.append(input())
    length=len(words[i])
    
    if length>=4 and words[i][0]!=words[i][length-1]:
        count=count+1
        print("")

print(words)
print(count)
