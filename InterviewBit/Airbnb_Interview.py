"""
http://xkcd.com/287/

"Mixed Fruit": 2.15
"French Fries": 2.75
"Side Salad": 3.35
"Hot Wings": 3.55
"Mozzarella Sticks": 4.20
"Sampler Plate": 5.80

"""

# def findItem(order, sum, menu):
#     print order, sum
#
#     if sum == totalSum:
#         return order
#
#     if sum < totalSum:
#         for key, price in menu.items():
#             sum += price
#             if sum < totalSum:
#                 print "sum < total", sum
#                 order.append(key)
#                 return findItem(order, sum, menu)
#             if sum > totalSum:
#                 print "sum > total", sum
#                 sum -= price
#
#     else:
#         return None

menu = {"Mixed Fruit": 2.15,
        "French Fries": 2.75,
        "Side Salad": 3.35,
        "Hot Wings": 3.55,
        "Mozzarella Sticks": 4.20,
        "Sampler Plate": 5.80}


def createOrder(menu, total):

    if not menu or not total:
        return []

    def checkMenu(menu, total, sum, order):

        for item, price in menu.items():

            if sum + price == total:
                print order, item
                return

            if sum + price <= total:
                order.append(item)
                checkMenu(menu, total, sum + price, order)
                order.remove(item)

    checkMenu(menu, total, 0, [])

createOrder(menu, 15.05)



