#----------* CHALLENGE 39 *----------
#Ask the user to enter a number between 1 and 12 and then display the times table for that number.

num = int(input("Enter a number between 1 and 12: "))

for i in range (1,11):
    print(num,"x",i,"=",num*i)
