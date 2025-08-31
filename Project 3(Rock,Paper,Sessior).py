import random
print("rock,paper,scissor")

option = ["rock","paper","scissor"]

friend = random.choice(option)

user = input("Your choice: ")

if user == friend:
    print("Its a draw!")

elif user == "paper" and friend == "rock":
    print(f"friend choose: {friend} and you choose {user}\nYou won!") 

elif user == "paper" and friend == "scissor":
    print(f"friend choose: {friend} and you choose {user}\nYou lose!") 

elif user == "rock" and friend == "paper":
    print(f"friend choose: {friend} and you choose: {user}\nYou lose!")

elif user == "rock" and friend == "scissor":
    print(f"friend choose: {friend} and you choose: {user}\nYou won!")

elif user == "scissor" and friend == "paper":
    print(f"friend choose: {friend} and you choose: {user}\nYou won!")

elif user == "scissor" and friend == "rock":
    print(f"friend choose: {friend} and you choose: {user}\nYou lose!")

