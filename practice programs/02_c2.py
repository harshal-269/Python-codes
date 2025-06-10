# sum of first n natural numbers

n = int(input("Enter any numer: "))
sum = 0
for i in range(0,n+1):
    sum = sum + i
print(f"sum of first {n} number is: ", sum)