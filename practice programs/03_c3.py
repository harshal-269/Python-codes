# factorial of n number using while loop

number = int(input("Enter any number: "))
fact = 1
i = 0
if(number > 0):

    while i < number:
        i = i + 1
        fact = fact * i
    print(f"Factorial of {number} is: ",fact)

else:
    print(f"Factorial of {number} is: 0")        