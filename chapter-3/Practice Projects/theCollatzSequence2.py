import sys


def collatz(number):
    if number % 2 == 0:
        return number // 2
    elif number % 2 == 1:
        return 3 * number + 1


print("Enter a number: ")

try:
    userNumber = int(input())
except ValueError as exception:
    print("Error: Invalid argument. Please enter a number.")
    print(exception)
    sys.exit(1)

newNumber = collatz(userNumber)

while userNumber != 0:
    print(newNumber)
    newNumber = collatz(newNumber)
    if newNumber == 1:
        print("1")
        break

print("Finished :)")
