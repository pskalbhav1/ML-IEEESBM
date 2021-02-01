list1 = ["a", "b", ["c", ["d", "e", ["f", "g"], "k"], "l"], "m", "n"] 
list2= ["h", "i", "j"]
list1[2][1][2].extend(list2)
print ("list is " + str(list1))