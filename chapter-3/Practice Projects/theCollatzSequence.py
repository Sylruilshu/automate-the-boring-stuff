def collatz(number: int) -> int | None:
    if number % 2 == 0:
        return number // 2
    elif number % 2 == 1:
        return 3 * number + 1


print("Enter a number: ")
userNumber = int(input())
collatzNumber = collatz(userNumber)

while userNumber != 0:
    print(collatzNumber)
    collatzNumber = collatz(collatzNumber)
    if collatzNumber == 1:
        print("1")
        break

print("Finished :)")

# should i print userNumber first?
