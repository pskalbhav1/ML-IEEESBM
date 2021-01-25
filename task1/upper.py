def words_game(str):

   count=0

   for i in range(len(str)):
       if str[i].isupper():
           count=count+1
   print(count)

words_game("01CoMputer07ScienCe")
