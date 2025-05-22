from random import randint

guess = []

comp = []

a = randint(0,9)
b = randint(0,9)
c = randint(0,9)
d = randint(0,9)

comp.append(a)
comp.append(b)
comp.append(c)
comp.append(d)



#print(comp)

Attempts = 0
while 1:

    guess = (list)(input("enter a 4 digit number:"))
    if len(guess) != 4:
        print("Please only enter a 4 digit number")
        continue
    
    Attempts += 1

    correct = 0
    wrong = 0
    int_guess = 0
    for i in range(0,4):

        int_guess = int(guess[i])

        if int_guess == comp[i]:
            correct += 1
        elif int_guess in comp:
            wrong += 1

    if correct == 4:
        print("You got it in", Attempts, "attempts! the answer was", a,b,c,d)
        break

    print(correct, "correct number(s) in correct place(s)")
    print(wrong, "correct number(s) in wrong place(s)")

        






















#if a == (int)(l[0]) or b == (int)(l[1]) or  c == (int)(l[2]) or  d == (int)(l[3]):
    #print("you win!")

#print(l[3])
#print(l[2])
#print(l[1])
#print(l[0])
































#thousands = (int)(guess/1000)
#guess = guess - thousands*1000
#hundreds = (int)(guess/100)
#guess = guess - thousands*100
#tens = (int)(guess/10)
#units = (int)guess/1)



#print(thousands)
#print(hundreds)
#print (tens)
#print (units)


