#----------* CHALLENGE 41 *----------
#Ask the user to enter their name and a number. If the number is less than 10, then display their name that
#number of times; otherwisedisplay the message “Too high” three times.

name = input("Enter your name: ")
num = int(input("Enter a number: "))

if num < 10:
    for i in range (1,num+1):
        print(name)
else:
    for i in range (1,4):
        print("Too High")