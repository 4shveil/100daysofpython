from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

money_machine = MoneyMachine()
menu = Menu()
coffee_maker = CoffeeMaker()

while True:
    user_choice = None
    while user_choice == None:
        user_choice = input(f"What would you like? ({menu.get_items()}): ").lower()
        if user_choice == "report":
            coffee_maker.report()
            money_machine.report()
            user_choice = None
            continue
        elif user_choice == "off":
            break
        else:
            drink = menu.find_drink(user_choice)
    
    if user_choice == "off":
        break

    resource_sufficient = coffee_maker.is_resource_sufficient(drink)
    payment_enough = money_machine.make_payment(drink.cost)

    if not resource_sufficient and payment_enough:
        print("Something went wrong, Try again.")
        continue
    
    coffee_maker.make_coffee(drink)
