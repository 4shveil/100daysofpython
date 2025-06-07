from random import choice
from art import logo

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
player_cards = []
dealer_cards = [11, 10, 1]

def deal_cards(caller, continuous):
    """Receives the deck of cards, and append the new cards to the deck, after doing so,
     it returns true if it's less than 21 or false if it's more than 21.
     :type continuous: boolean
     :type caller: list"""
    if continuous:
        while deck_sum(caller) < 16:
            caller.append(choice(cards))
            print("Dealer has drawn a card.")
            print(show_decks())
            if deck_sum(caller) > 16:
                return check_end()
        return None

    if not caller and caller == player_cards:
        for i in range(2):
            caller.append(choice(cards))
    else:
        caller.append(choice(cards))
        return check_end()


def show_decks():
    """Receives the deck of cards and return out the result to the screen."""
    return (f"Your deck is: {player_cards} with a total sum of your deck is: {deck_sum(player_cards)}\n"
            f"Dealer deck is: {dealer_cards} with a total sum of your deck is: {deck_sum(dealer_cards)}\n")


def deck_sum(caller_deck):
    """Receives the caller deck and returns the total sum of the deck."""
    total_sum = 0
    for card in caller_deck:
        total_sum += card
    return total_sum


def check_end():
    if not check_blackjack() == -1:
        print("\n" * 1000)
        if check_blackjack() == 0:
            print(show_decks())
            print("It's a draw. No one wins.")
        return True

    if deck_sum(player_cards) > 21:
        if 11 in player_cards:
            ace_index = player_cards.index(11)
            player_cards[ace_index] = 1
            return check_end()
        print("\n" * 1000)
        print(show_decks())
        print("You went over 21. Busted.")
        return True

    if deck_sum(dealer_cards) > 21:
        if 11 in dealer_cards:
            ace_index = dealer_cards.index(11)
            dealer_cards[ace_index] = 1
            return check_winner(player_cards,dealer_cards)
        print("\n" * 1000)
        print(show_decks())
        print("Dealer went over 21. You win.")
        return True

    return False


def check_winner(_,__):
    deal_cards(dealer_cards, True)

    if deck_sum(player_cards) > deck_sum(dealer_cards):
        print("You win.")
        return True
    elif deck_sum(player_cards) == deck_sum(dealer_cards):
        print("It's a draw.")
        return True
    elif deck_sum(player_cards) < deck_sum(dealer_cards) and deck_sum(dealer_cards) <= 21:
        print("Dealer wins.")
        return True

    return None



def check_blackjack():
    """Returns 1 if there is a blackjack 0 if it's a draw, -1 otherwise.
    It also prints out if it's a blackjack, and by whom this blackjack is. E.g: A player blackjack.
    OBS: It does not print anything if it's a draw. Simply returns 0"""
    player_sum = deck_sum(player_cards)

    if player_sum == 21:
        deal_cards(caller=dealer_cards, continuous=True) ## Deals the dealer second card for a chance of a draw
        if not deck_sum(dealer_cards) == 21:
            print(f"{show_decks()}\nIt's a player blackjack. Player wins!")
            return 1
        else:
            return 0

    if deck_sum(dealer_cards) == 21:
        if not player_sum == 21:
            print(f"{show_decks()}\nIt's a dealer blackjack. Player loses!")
            return 1
        else:
            return 0

    return -1


def reset_game():
    global player_cards, dealer_cards
    player_cards = []
    dealer_cards = []
    print(logo)


def blackjack():
    keep_drawing = True

    choices = {
        'h': deal_cards,
        's': check_winner,
    }
    deal_cards(player_cards, False)
    deal_cards(dealer_cards, False)
    print(show_decks())
    if check_end():
        keep_playing = input("Do you wish to keep playing? 'Yes' to keep playing").lower().strip()
        if keep_playing == "yes":
            reset_game()
            blackjack()

    while keep_drawing:
        player_choice = input("Do you hit, stand or fold?\n'h' to hit, 's' to stand 'f' to fold: ").lower().strip()
        if player_choice not in ['h', 's', 'f'] or (deck_sum(player_cards) < 11 and player_choice == 's'):
            print("Invalid option. Please try again. (Perhaps you have less than 11 and is trying to stand?)")
            continue
        if choices.get(player_choice)(player_cards, False):
            keep_playing = input("Do you wish to keep playing? 'Yes' to keep playing").lower().strip()
            if keep_playing == "yes":
                keep_drawing = False
                reset_game()
                blackjack()
        else:
            print(show_decks())

blackjack()
