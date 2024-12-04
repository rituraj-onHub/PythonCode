import random

user_wins = 0
comp_wins = 0

option = ["rock","paper","scissor"]

while True:
    user_choice = input("Choice Rock/Paper/Scissors or q for Quit :").lower()
    if user_choice == "q":
        break

    if user_choice not in option :
        continue

    random_num = random.randint(0,2) # here 0 = rock, 1 = paper , 2 = scissor
    comp_choice = option[random_num]

    print("Computer pick",comp_choice)

    if user_choice == "rock" and comp_choice == "scissor":
        print("you won!")
        user_wins +=1
    elif user_choice == "scissor" and comp_choice == "paper":
        print("you won!")
        user_wins +=1
    elif user_choice == "paper" and comp_choice == "rock":
        print("you won!")
        user_wins +=1
    elif user_choice == comp_choice :
        print("both picked the same ")
    else :
        print("computer won!")
        comp_wins+=1

print(f"You won {user_wins} times")
print(f"Computer won {comp_wins} times.")
print("GoodBye!")