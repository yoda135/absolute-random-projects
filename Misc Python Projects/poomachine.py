
print("#############################")
print("#      THE POO MACHINE      #")
print("#############################")

myname = input("What is your name:")
mynum = int(input("Give me a number:"))

if mynum > 100:
    print("Number too high")
else :
    for i in range(mynum):
        print (myname, "just had poo number:", i)

    print(myname, "Has finally finished pooing")
