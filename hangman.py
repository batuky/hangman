# from word import word     if you want to input word manually, active it!
import random

#word coming from wordlist.txt
with open('wordlist.txt','r') as f:
    words = f.readlines()
# because of \n i did -1 
word = random.choice(words)[:-1]

#i can do some mistake 
error_num = 6 

guesses = []
done = False

#its changing letters to _  
while not done:
    for letter in word:
        if letter.lower() in guesses:
            print(letter, end=" ")
        else:
            print("_",end=" ")
    print("")

#main part 
    guess = input(f"allowed error number :{error_num} left. \n Next Guess:")
    guesses.append(guess.lower())

    if guess.lower() not in word.lower():
        error_num -=1 
        if error_num == 0:
            break

    
    done = True
    for letter in word:
        if letter.lower() not in guesses:
            done = False


if done:
    print(f"You find it! it was {word}" )
else:
    print(f"You could not find it! it was {word} ")
