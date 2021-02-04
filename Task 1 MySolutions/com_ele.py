set1 = {10, 20, 30, 40, 50}
set2 = {60, 70, 80, 90, 10}

set3=set1.intersection(set2)
if len(set3)==0:
    print("No common elements")
else:
    print(set3)