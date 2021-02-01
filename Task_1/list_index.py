List1 = [ "Pro", "t", "b", "pa", "o", "IEEE", "fam"]
List2 = [ "ud", "o", "e", "rt", "f", "SBM", "ily"]
res = [i + j for i, j in zip(List1, List2)]
print("The concatenated lists: " + str(res))