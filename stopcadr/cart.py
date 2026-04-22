cart = []

def add_to_cart(product_id):
    cart.append(product_id)
    return cart

def get_cart():
    return cart

def clear_cart():
    cart.clear()
    return cart
