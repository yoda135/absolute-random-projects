
print("#############################")
print("#      THE POO MACHINE      #")
print("#############################")

while 1:
    myname = input("What is your name:")
    mynum = int(input("Give me a number between 1 and 100:"))

    if mynum > 100:
        print(mynum, "is too many poos")
        print("\n\n")
    else :
        for i in range(mynum):
            print (myname, "just had poo number:", i+1)

        print(myname, "Has finally finished pooing")
        print("\n\n")
