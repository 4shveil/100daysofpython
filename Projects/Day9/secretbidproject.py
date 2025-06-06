from art import logo

print(logo)

bids = {}

def bidders_data_creation():
    global bids
    first_name = input("What is your name?: ")
    bid_amount = int(input("What is your bid?: $"))
    bids = {first_name: bid_amount}

def find_winner():
    highest_bid = max(bids.values())
    highest_bidder = ""
    for key, value in bids.items():
        if value == highest_bid:
            highest_bidder = key

    print(f"The winner is {highest_bidder} with a bid of ${highest_bid}")

while True:
    bidders_data_creation()
    still_bidders = input("Is there any other bidders? 'y' for yes or 'n' for no: ")
    if still_bidders == "n":
        break
    print("\n" * 1000)

find_winner()
