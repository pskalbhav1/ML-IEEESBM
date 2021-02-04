list1 = ["a", "b", ["c", ["d", "e", ["f", "g"], "k"], "l"], "m", "n"]
list2=  ["h", "i", "j"]

list1[2][1][2].append(list2)
print("The new list is ", list1)