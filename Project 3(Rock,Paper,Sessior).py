import random
print("rock,paper,scissor")

option = ["rock","paper","scissor"]

computer = random.choice(option)

user = input("Your choice: ")

if user == computer:
    print("Its a draw!")

elif user == "paper" and computer == "rock":
    print(f"Computer choose: {computer} and you choose {user}\nYou won!") 

elif user == "paper" and computer == "scissor":
    print(f"Computer choose: {computer} and you choose {user}\nYou lose!") 

elif user == "rock" and computer == "paper":
    print(f"computer choose: {computer} and you choose: {user}\nYou lose!")

elif user == "rock" and computer == "scissor":
    print(f"computer choose: {computer} and you choose: {user}\nYou won!")

elif user == "scissor" and computer == "paper":
    print(f"computer choose: {computer} and you choose: {user}\nYou won!")

elif user == "scissor" and computer == "rock":
    print(f"computer choose: {computer} and you choose: {user}\nYou lose!")

