
from random import randint

secret = randint (0,500)

for x in range(0, 20):
    guess = int(input("enter a number "))

    if guess == secret:
        print ("well done you've won 100 pounds!")

    if guess < secret:
        print ("your guess is to low")    
                  
    if guess > secret:
         print ("your guess is to high")
   
         
                   


















 
