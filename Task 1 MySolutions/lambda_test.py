List = [ 20, 67, 385 ,165 , 52, 33, -19 , 0 , -220 , -66]

check= lambda a: a%33==0 or a%55==0

i=0
while i<len(List):
    if check(List[i]):
        print(List[i], end=" ")
    i+=1


# Alternate way:-
# check= lambda x: x%33==0 or x%55==0
# for x in List:
    
#     if check(x):
#         print(x, end=" ")