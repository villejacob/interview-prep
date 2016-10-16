'''
Question:
https://xkcd.com/287/
'''
menu = {"Mixed Fruit"       : 2.15,
        "French Fries"      : 2.75,
        "Side Salad"        : 3.35,
        "Hot Wings"         : 3.55,
        "Mozarella Sticks"  : 4.20,
        "Sampler Plate"     : 5.80}

def findSum(menu, total):

    possible_orders = []

    def makeOrder(menu, total, sum, order):

        # If the current order meets the condition
        if sum == total:
            # Sort the order to find duplicates
            order = sorted(order)
            if order not in possible_orders:
                # Add to non-locally defined order list
                possible_orders.append(order)
            return

        # Iterate through the menu dictionary
        for item, price in menu.items():
            # When the next item could be added to the order
            if sum + price <= total:
                # Add the item and call the method again
                # order.append(item)
                makeOrder(menu, total, sum + price, order + [item])
                # when order.append()
                # makeOrder(menu, total, sum + price, order)
                # backtracking when the item didn't make the cut
                # order.remove(item)

    makeOrder(menu, total, 0, [])
    return possible_orders

final_orders = findSum(menu, 15.05)
for order in final_orders:
    print order