import csv


for i in range (0,10):

    q = input("say something ")

    with open('hangman.csv') as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        for row in readCSV:
            if row[0] == q:
                print(row[1])
