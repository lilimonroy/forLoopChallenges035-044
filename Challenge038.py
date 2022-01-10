#----------* CHALLENGE 38 *----------
#Change program 037 to also ask for a number. Display their name (one letter at a time on each line) 
# and repeat this for the number of times they entered.

name = input("Enter name: ")
num = int(input("Enter a number: "))

for x in range (0,num): #First loop refers to THE TIMES THE WORD COMPLETE REPEATS
    for i in name: #Second loop display every letter in the round it's now ('x' variable)
        print(i)
