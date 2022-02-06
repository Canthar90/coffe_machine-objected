from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
import time


coffe_menu = MenuItem
payment = MoneyMachine()
menu=Menu()
coffe_making = CoffeeMaker()
mane_flag = False
while not mane_flag:
    order=input(f"What would you like? ({menu.get_items()}): ").lower()
    if order == 'espresso' or order == 'latte' or order == 'cappuccino':
        coffe_making_resources = menu.find_drink(order)
        coffe_making_flag = coffe_making.is_resource_sufficient(coffe_making_resources)
        if coffe_making_flag:
            payment_flag = payment.make_payment(coffe_making_resources.cost)
            if payment_flag:
                coffe_making.make_coffee(coffe_making_resources)
    elif order == 'report':
        coffe_making.report()
        payment.report()
    elif order == 'off':
        print('Turning off the coffee machine bye.')
        time.sleep(4)
        mane_flag = True