#!/usr/bin/env python3

"""
Based off of: http://inst.eecs.berkeley.edu/~cs188/sp09/pacman.html

To run this script, type:

  python3 buyLotsOfFruit.py

Once you have correctly implemented the buyLotsOfFruit function,
the script should produce the output:

Cost of [('apples', 2.0), ('pears', 3.0), ('limes', 4.0)] is 12.25
"""

FRUIT_PRICES = {
    'apples': 2.00,
    'oranges': 1.50,
    'pears': 1.75,
    'limes': 0.75,
    'strawberries': 1.00
}

def buyLotsOfFruit(orderList):
    """
    orderList: List of (fruit, weight) tuples

    Returns cost of order
    """
    # *** Your Code Here ***
    # Multiply weight by standard fruit price to get cost. Add up costs.
    # If a fruit in the list doesn't appear in FRUIT_PRICES, print an error message and return None
    totalCost = 0
    for order in orderList:
        fruit = order[0]
        weight = order[1]
        
        if fruit in FRUIT_PRICES:
            price = FRUIT_PRICES[fruit]
            cost = weight * price
            totalCost += cost
        else:
            print("Error: a fruit could not be found in FRUIT_PRICES")
            return None
    return totalCost

def main():
    orderList = [
        ('apples', 2.0),
        ('pears', 3.0),
        ('limes', 4.0)
    ]

    print("Cost of %s is %s." % (orderList, buyLotsOfFruit(orderList)))

if __name__ == '__main__':
    main()
