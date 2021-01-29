List1 = [ 'Pro', 't', 'b', 'pa', 'o', 'IEEE', 'fam']
List2 = [ 'ud', 'o', 'e', 'rt', 'f', 'SBM', 'ily']
print("Given list 1: ", List1)
print("Given list 2: ",List2)

List3 = [i + j for i, j in zip(List1, List2)]

print("The concatenated list is: ",List3)

