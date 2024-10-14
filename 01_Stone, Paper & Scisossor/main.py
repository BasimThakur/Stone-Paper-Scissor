import random

#stone paper scisossor

'''
1 for stone
-1 for paper
0 for scisossor

'''

computer = random.choice([1, -1, 0])
youStr = input("Enter your choice (st, p or sc?) : ")
youDict =  {"st": 1, "p": -1, "sc": 0}
reverseDict = {1 : "Stone", -1 : "Paper", 0 : "Scisossor"}

you = youDict[youStr]

# By now we have 2 numbers (variables), 'you' and 'computer'

print(f"You chose {reverseDict[you]}\nComputer chose {reverseDict[computer]}")

if(computer == you):
    print("Its a Draw!!!")

else:
    if(computer == -1 and you == 1):
        print("Computer Win!")  

    elif(computer == -1 and you == 0):
        print("You Win!") 

    elif(computer == 1 and you == -1):
        print("You Win!")  

    elif(computer == 0 and you == -1):
        print("Computer Win!")  

    elif(computer == 1 and you == 0):
        print("Computer Win!")  

    elif(computer == 0 and you == 1):
        print("You Win!")  

    else:
        print("Something went wrong")