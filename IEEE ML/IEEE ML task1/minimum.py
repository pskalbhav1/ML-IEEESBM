# Q.9 minimum
import time
while True:
    l1=[]
    n=int(input("Enter the amount of numbers :"))
    if (n<5):
        print("Enter more than 5 numbers")
    else:
        for i in range(n):
            num=int(input("Enter the number"))
            l1.append(num)
        l1.sort()
        print(l1[2])
        time.sleep(3) #i wanted a time delay, otherwise the quit prompt would come suddenly.
        quit()
