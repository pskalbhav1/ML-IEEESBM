name = input("Enter name :")
age = int(input("Ente age :"))
if (age < 0):
    print("Enter a valid age ")
elif (0 < age < 18):
    print(name.lower())
elif (18 <= age < 30):
    print(name.capitalize())
elif (age >= 30):
    print(name.upper())
else:
    ("Enter a valid age ")
