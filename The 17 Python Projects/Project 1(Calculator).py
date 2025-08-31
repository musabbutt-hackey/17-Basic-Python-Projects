print("! Mini Calculator")

print("press + for addition\npress - for subtraction\npress * for multiply\npress / for divide")


num1 = float(input("Enter 1st number: "))
choice = (input("Enter Your Choice: +,-,*,/"))
num2 = float(input("Enter 2nd number: "))


if choice == "+":
    print("result:",num1+num2)

elif choice == "-":
   print("Result:", num1-num2) 

elif choice == "*":
    print("Result:",num1*num2)

elif choice ==  "/":
    print("Result:", num1/num2)

else:
    print("Enter a number.Not a" "Alphabet")
