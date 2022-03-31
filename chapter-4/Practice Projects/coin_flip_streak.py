import random

def generate_random_coin_flips():
    coin_flips = []

    for i in range(100):
        if random.randint(0, 1) == 0:
            coin_flips.append('H')
        else:
            coin_flips.append('T')
    return coin_flips

def count_number_of_streaks(coin_flips):
    coin_flips_string = ''.join(coin_flips)
    number_of_streaks = coin_flips_string.count('HHHHHH') + coin_flips_string.count('TTTTTT')
    return number_of_streaks

result = 0

# TODO: Calculation may be inaccurate.
for experimentNumber in range(10000):
    coin_flips = generate_random_coin_flips()
    number_of_streaks = count_number_of_streaks(coin_flips)

    result += number_of_streaks
    
print(f'Chance of streak: {result/10000}%')