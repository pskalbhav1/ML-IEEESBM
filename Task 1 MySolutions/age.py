value=input().split()

age=int(value[0])
name=value[1]

if age>0 and age<=18:
    name=name.lower()
elif age>18 and age<=30:
    name=name.capitalize()
else:
    name=name.upper()

print(name)