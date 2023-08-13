import random

wiords_list=["abeer","safa","shahba"]

try_=6
chosen_word= random.choice(wiords_list)

blank=[]
print(*blank)
print(chosen_word)
 

lengh=len(chosen_word)

for b in range(lengh):
  blank +="_"

print(blank)

while try_>0:
    letter=input("Enter letter")
    if letter in chosen_word:
       for i in range(lengh):
          if chosen_word[i]==letter:
             blank[i]=letter
             print(blank)
             if ("_" not in blank):
                print ("done")
    else:
     try_-=1
     if try_==0:
       print("failed")
  



# def input_letter():
#    letter=input("Enter letter")[0]
#    try_=6


#    if letter in chosen_word:
#     print("true")
#     blank_new=len(blank)-1
#     if blank_new==0:
#         print("haaaaaaay win")
#     else:
#         input_letter()


#    else:
#     try_ -=1

#     if try_==0:
#         print("game over")
#     else:
#        input_letter()


# input_letter()








       

