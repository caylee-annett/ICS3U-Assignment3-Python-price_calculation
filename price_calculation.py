#!/usr/bin/env python3

# Created by: Caylee Annett
# Created on: May 2021
# This program calculates the total cost with HST and a discount if qualified


import random
import constants


def main():
    # This calculates the total cost

    # Input
    print("This program calculates your total cost, including HST "
          "and a discount if the cost is $1000 or more.")
    number_of_items = int(input(
        "Enter the quantity of items you are purchasing (each item is "
        "$100): "))
    print("")

    # Process & Output
    if number_of_items >= 10:
        subtotal = number_of_items * constants.PRICE
        discounted_price = subtotal - subtotal * constants.DISCOUNT
        total = discounted_price + discounted_price * constants.HST
        print("The subtotal with the discount is ${0:,.2f}. The total "
              "including HST is ${1:,.2f}.".format(discounted_price, total))

    else:
        subtotal = number_of_items * constants.PRICE
        total = subtotal + subtotal * constants.HST
        print("The subtotal is ${0:,.2f}. The total including HST "
              "is ${1:,.2f}.".format(subtotal, total))
    print("\nDone.")


if __name__ == "__main__":
    main()
