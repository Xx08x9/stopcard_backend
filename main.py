# cart = {}

# def add_to_cart(cart, item, quantity):
#     if item in cart:
#         cart[item] += quantity
#     else:
#         cart[item] = quantity

# def remove_from_cart(cart, item):
#     if item in cart:
#         del cart[item]

# def update_quantity(cart, item, quantity):
#     if item in cart:
#         if quantity <= 0:
#             del cart[item]
#         else:
#             cart[item] = quantity

# def get_total(cart, prices):
#     total = 0
#     for item, qty in cart.items():
#         total += prices[item] * qty
#     return total

# prices = {
#     "apple": 10,
#     "banana": 5,
#     "orange": 7
# }
# add_to_cart(cart, "sony", 2)
# add_to_cart(cart, "Canon", 3)

# print(cart)
# print(get_total(cart, prices))

if __name__ == "__main__":
    cart = {}
    add_to_cart(cart, "sony_a7", 2)
    add_to_cart(cart, "canon_r5", 3)

    print(cart)
    print(get_total(cart, prices))