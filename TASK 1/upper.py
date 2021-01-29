def Count(str): 
    upper = 0
    for i in range(len(str)): 
        if str[i].isupper(): 
            upper += 1
    
    print('Upper:', upper) 

str = input("Enter string : ")   
Count(str) 
