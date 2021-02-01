def uppercase(str1) :
    cnt=0
    for i in str1:
        if i.isupper()==1:
            cnt+=1
    return cnt
str2=input("Enter the string \n")
num=uppercase(str2)
print(num)