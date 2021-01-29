def division(num):
    return lambda a: a%num

list1 = []
num=int(input("enter the numbers of elements in the list:"))

for j in range(1,num):
    ele = int(input("Enter elements:"))
    list1.append(ele)
   
for i in range(0,len(list1)):
    division55= division(55)
    division33= division(33)
    if(division55(list1[i])==0 or division33(list1[i])==0):
       print(list1[i])
