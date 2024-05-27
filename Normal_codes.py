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

profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

class CoffeeMachineNew:

    def is_resource_sufficient(self,order_ingredients):
        is_enough = True
        for item in order_ingredients:
            if order_ingredients[item] >= resources[item]:
                print(f"Sorry there is not enough {item}.")
                is_enough = False
        return is_enough


    def process_coins(self):
        """returns the total calculated for coins inserted"""
        print("please insert coins.")
        total = int(input("how many quarters? ")) * 0.25
        total += int(input("how many dimes? ")) * 0.10
        total += int(input("how many nickles? ")) * 0.05
        total += int(input("how many pennies? ")) * 0.01
        return total


    def is_transaction_successful(self,money_received, drink_cost):
        """returns true whe the payment is accepted or False if the money is insufficient"""
        if money_received > drink_cost:
            change = round(money_received - drink_cost, 2)
            print(f"Here is ${change} change")
            global profit
            profit += drink_cost
            return True
        else:
            print("sorry! that's not enough money😒. Money refunded ")
            return False


    def make_coffee(self,drink_name, order_ingredients):
        """deduct the required ingredients from the resources"""
        for item in order_ingredients:
            resources[item] -= order_ingredients[item]
        print(f"Here is your {drink_name}☕")


    # is_on = True
    # while is_on:
    #     user_choice = input("What would you like? (espresso/latte/cappuccino):  ")
    #     if user_choice == "end":
    #         is_on = False
    #         print("thank you")
    #     elif user_choice == "report":
    #         print(f"water: {resources['water']}ml")
    #         print(f"milk: {resources['milk']}ml")
    #         print(f"coffee: {resources['coffee']}g")
    #         print(f"Money: ${profit}")
    #     else:
    #         drink = MENU[user_choice]
    #         if is_resource_sufficient(drink["ingredients"]):
    #             payment = process_coins()
    #             if is_transaction_successful(payment, drink['cost']):
    #                 make_coffee(user_choice, drink["ingredients"])