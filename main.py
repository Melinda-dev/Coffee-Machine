from MENU import *


def update_resource(your_choice):
    """
    this function is used to update the resources after making an ordered coffee
    input: an order in the menu
    ourtput: return the updated resources
    :param your_choice:
    :return:
    """

    resources["water"] = resources["water"] - our_menu[your_choice]["ingredients"]["water"]
    resources["milk"] = resources["milk"] - our_menu[your_choice]["ingredients"]["milk"]
    resources["coffee"] = resources["coffee"] - our_menu[your_choice]["ingredients"]["coffee"]
    return resources

def print_report():
    """
    print current resources in required format.
    :return:
    """
    print(f"Water: {resources['water']}")
    print(f"milk: {resources['milk']}")
    print(f"coffee: {resources['coffee']}")


def check_sufficient(v_order):
    """
    This function use to check if the resource is enough to make an ordered coffee.
    input: an order in the menu
    output: True or exit when the ingredient is not enough.
    :return:
    """
    if (
        resources["water"] >= our_menu[v_order]["ingredients"]["water"] and
        resources["milk"] >= our_menu[v_order]["ingredients"]["milk"] and
        resources["coffee"] >= our_menu[v_order]["ingredients"]["coffee"]
    ):
        return True
    else:
        print("Sorry we have not enough ingredient")
        exit()


def get_your_payment():
    your_quarters = int(input("How many quarters?:"))
    your_dimes = int(input("How many dimes?:"))
    your_nickles = int(input("How many nickles?:"))
    your_pennies = int(input("How many pennies?:"))
    your_payment = your_dimes * 10 + your_nickles * 5 + your_pennies * 1 + your_quarters * 25
    return your_payment


def cal_changes(your_payment, our_order):
    if your_payment > our_menu[our_order]["cost"]:
        your_changes = your_payment - our_menu[our_order]["cost"]
        print(your_changes)
        print("Collect your changes please!")
        return your_changes

    else:
        print("your money is not enough. Sorry!")
        return 0


machine_off = False

while not False:

    our_order = input("What would you like?(espresso/latte/cappuccino):")
    print_report()

    check_sufficient(our_order)
    print("Please insert coins.")

    if cal_changes(get_your_payment(), our_order) == 0:
        break

    update_resource(our_order)



