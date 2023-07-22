from cs50 import get_float


def main():

    dollars = get_change()
    cents = round(100 * dollars)    # converts dollars to cents
    coins = 0

    # calculates minimum number of coins to return change
    coins = cents // 25
    cents = cents % 25

    coins += cents // 10
    cents = cents % 10

    coins += cents // 5
    cents = cents % 5

    coins += cents
    print(coins)


# Prompts user for change owed
def get_change():

    while True:
        n = get_float("Change owed: ")
        if n > 0:     # condition to check for positive input
            break
    return n


main()