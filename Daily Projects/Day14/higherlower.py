from random import choice
from game_data import data
from art import logo, vs

print(logo)

compare_a = choice(data)
score = 0


def display_values(data_a, data_b) -> None:
    """
    Take two dictionaries and display them. Formated for the higher lower game
    :rtype: None
    """
    print(f"Compare A: {data_a["name"]}, a {data_a["description"]}, from {data_a["country"]}")
    print(vs)
    print(f"Compare B: {data_b["name"]}, a {data_b["description"]}, from {data_b["country"]}")


def compare_followers(data_a, data_b ):
    if data_a["follower_count"] > data_b["follower_count"]: # assuming no equal values exist
        return 'a'
    else:
        return 'b'


while True:
    compare_b = choice(data)

    display_values(compare_a, compare_b)

    who_has_more = compare_followers(compare_a, compare_b)

    user_guess = input("Who has more followers? Type 'A' or 'B': ").lower()

    if user_guess != who_has_more:
        print("\n" * 1000 + f"{logo}")
        print(f"You lost. Compare {who_has_more.upper()} had more followers.")
        break

    score += 1
    print(f"You're right! Current score: {score}")
    print("\n" * 1000 + f"{logo}")
    compare_a = compare_b
