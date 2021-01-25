#Q.7 upper
x=input("Enter the string : ")
isalnum=x.isalnum()
if (isalnum==1):
    count=0
    for i in (x):
        if i.isupper():
            count=count+1
    print(count)
else:
    print("ONLY ALPHANUM CHARACTERS ARE ACCEPTABLE")
    
