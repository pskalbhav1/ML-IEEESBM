n=int(input("Enter the no of people\n"))
dic={}
for i in range(n):
    value= int(input("Enter the age \n"))
    key= input("Enter the name \n")
    dic[key]=value
for i in dic:
    if dic[i]<18 :
        j=i.lower()
        print(j)
    elif dic[i]>18 and dic[i]<30:
        j=i.capitalize()
        print(j)
    elif dic[i]>30:
        j=i.upper()
        print(j)
   