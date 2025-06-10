MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = dict(water=300, milk=200, coffee=100, total_money=0.0)

def show_report():
    water = resources["water"]
    milk = resources["milk"]
    coffee = resources["coffee"]
    money = resources["total_money"]

    print(f"Water: {water}\nMilk: {milk}\nCoffee: {coffee}\nTotal Money: ${"{:.2f}".format(money)}")


def order_management(order):
    if order == "report":
        show_report()
        return

    make_coffee(order)


def check_resources(order):
    enough_resources = True
    if order == "espresso":
        for keys in MENU["espresso"]["ingredients"]:
            if resources[keys] < MENU[order]["ingredients"][keys]:
                print(f"Sorry, we don't have enough {keys}")
                enough_resources = False
        return enough_resources

    for keys in resources:
        if keys == "total_money":
            continue

        if resources[keys] < MENU[order]["ingredients"][keys]:
            print(f"Sorry, we don't have enough {keys}")
            enough_resources = False

    return enough_resources


def process_money(order):
    user_money = 0.0
    available_coins = dict(quarters=0.25, dimes=0.10, nickels=0.05, pennies=0.01)
    drink_cost = MENU[order]["cost"]

    for key in available_coins:
        amount_of_coins = int(input(f"How many {key} do you put in the machine?: "))
        user_money += amount_of_coins * available_coins[key]

    if user_money < drink_cost:
        print("Sorry that's not enough money. Money refunded.")
        return False

    if user_money > drink_cost:
        change = user_money - drink_cost
        user_money -= change
        print(f"Here is ${"{:.2f}".format(change)} dollars in change.")

    resources["total_money"] += user_money

    return True


def make_coffee(order):
    espresso = False
    enough_resources = check_resources(order) and process_money(order)


    if not enough_resources:
        main()

    if order == "espresso":
        for keys in MENU["espresso"]["ingredients"]:
             resources[keys] -= MENU[order]["ingredients"][keys]
             espresso = True

    for keys in resources:
        if keys == "total_money" or espresso:
            break

        resources[keys] -= MENU[order]["ingredients"][keys]

    print(f"Here is your {order}! Enjoy!")


def main():
    while True:
        user_order = input(f"What would you like? {list(MENU.keys())}: ").lower().strip()

        if user_order == "off":
            break

        order_management(user_order)

main()
