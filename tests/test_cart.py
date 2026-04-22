from main import add_to_cart, remove_from_cart, update_quantity, get_total

def test_add_to_cart():
    cart = {}
    add_to_cart(cart, "sony_a7", 2)
    assert cart["sony_a7"] == 2

def test_remove_from_cart():
    cart = {"canon_r5": 1}
    remove_from_cart(cart, "canon_r5")
    assert "canon_r5" not in cart

def test_update_quantity():
    cart = {"gopro_hero": 1}
    update_quantity(cart, "gopro_hero", 3)
    assert cart["gopro_hero"] == 3

def test_get_total():
    cart = {"sony_a7": 2}
    prices = {"sony_a7": 1200}
    assert get_total(cart, prices) == 2400