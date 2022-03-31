import random


def generate_random_coin_flips(amount_of_flips):
    coin_flips = []

    for i in range(amount_of_flips):
        if random.randint(0, 1) == 0:
            coin_flips.append("H")
        else:
            coin_flips.append("T")
    return coin_flips


def count_number_of_streaks(coin_flips):
    coin_flips_string = "".join(coin_flips)
    number_of_streaks = coin_flips_string.count("HHHHHH") + coin_flips_string.count(
        "TTTTTT"
    )
    return number_of_streaks


print("Enter number of flips:")
amount_of_flips = int(input())

result = 0

for experimentNumber in range(10000):
    coin_flips = generate_random_coin_flips(amount_of_flips)
    number_of_streaks = count_number_of_streaks(coin_flips)

    result += number_of_streaks / amount_of_flips

print(result)
print(f"Chance of streak: {result/100}%")
