def collatz(number):
    if number == 1 or number == 0:
        return
    if number % 2 == 0:
        number = number // 2
        print(number)
    elif number % 2 == 1:
        number = 3 * number + 1
        print(number)
    collatz(number)


print("Enter a number: ")
userNumber = int(input())
collatzNumber = collatz(userNumber)
