name=input("enter your name")
age=int(input("enter your age"))

if age<18:
    print(name)
elif age in range(18,30):
    print(str(name[0].upper())+str(name[1:]))
else:
    print(name.upper())

