from random import randint
print("guess the number between 1, 100")

computer = randint(1, 100)

while True:
    user = int(input("guess a number: "))
    
    if user == computer:
        print("You Won!")
        break

    elif user > computer:
        print("Choose lower!")

    elif user < computer:
        print('Choose higher!')

    elif user >= 101:
        print("Choose between 1, 100")

   