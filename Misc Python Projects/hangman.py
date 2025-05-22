from random import randint
from man import draw_man
import csv

def draw_word(Word, Corrects, Wrongs):

    drawstr = ""
    all_good = True
    
    for i in range(len(Word)):
        if Word[i] in Corrects:
            drawstr = drawstr + Word[i]
            drawstr = drawstr + " "
        else:
            drawstr = drawstr + "_ "
            all_good = False

    print("Correct Guesses:\n")
    print(drawstr, " (", len(Word), " characters )")
    print("\n")

    w_str = ""
    print("Wrong Guesses:\n")
    for i in range(len(Wrongs)):
        w_str = w_str + str(Wrongs[i])
        w_str = w_str + " "

    print(w_str)
    print("\n")
    return all_good


  

def test_guess(Guess, Word):
    for i in range(len(Word)):
        if str(Word[i]) == str(Guess[0]):
            return True

    return False


word = ""

with open('hangman.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    row_count = sum(1 for row in readCSV)

secret = randint (0,row_count-1)
j = 0

with open('hangman.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    for row in readCSV:
        if j == secret:
            word = row[0]
            break
        else:
            j = j + 1

        
word = word.lower()
Attempts = 1
real_attempts = 0
corrects = []
wrongs = []
print("\n" * 40)
print("=======================")
print("====Sams Hangman=======")
print("=======================")

print(row_count, "Possible Words!!!\n\n")

draw_word(word,corrects,wrongs)

while (1):


    guess = input("Whats your guess:")
    guess = guess.lower()
    guess = guess.strip()
    if len(guess) == 0:
        print("you haven't typed in anything please try again!")
        continue

    if guess in corrects:
        print("you've already typed that silly!")
        continue
    if guess in wrongs:
        print("you've already typed that silly!")
        continue
    if guess.isalpha() != True:
        print("Only alphabet characters are allowed!")
        continue
    

    real_attempts = real_attempts + 1   

    if test_guess(guess, word) == True:
        corrects.append(guess)
    else:
        wrongs.append(guess)
        Attempts = Attempts + 1

    draw_man(Attempts-1)
    if draw_word(word,corrects,wrongs) == True:
        print("You have won :) in ", real_attempts, "Attempts")
        break        

    if Attempts > 14:
        print("You have lost :( the word was:", word);
        break
    else:
        print("this is attempt",real_attempts+1)
        print("\n")
    

