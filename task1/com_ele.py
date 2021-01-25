set1 = [10, 20, 30, 40, 50]
set2 = [60, 70, 80, 90, 10]
common_element=list()
for i in range(0,len(set1)):
    for j in range(0,len(set2)):
        if set1[i]==set2[j]:
          common_element.append(set1[i])
print(common_element)
