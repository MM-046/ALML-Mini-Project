def create_cart(owner, discount=0):
    """
    Creates a cart dictionary. discount=0 is an immutable default (int),
    which is completely safe to use.
    """
    return {"owner": owner, "items": [], "discount": discount}


def add_to_cart(cart, name, price, qty=1):
    """Appends a new item dictionary to the cart's mutable items list."""
    item = {"name": name, "price": price, "qty": qty}
    cart["items"].append(item)


def update_price(price_tuple, new_price):
    """Attempts to modify a tuple element. This WILL raise a TypeError."""
    try:
        price_tuple[0] = new_price 
    except TypeError as e:
        print(f"\n[X] Caught Expected Error in update_price: {e}")
        print("    Explanation: Tuples are immutable. Once created, their elements cannot be changed or reassigned.")


def calculate_total(cart):
    """Calculates total price, applies percentage discount, and returns final total."""
    raw_total = 0
    for item in cart["items"]:
        raw_total += item["price"] * item["qty"]
        
    discount_amount = raw_total * (cart["discount"] / 100)
    final_total = raw_total - discount_amount
    return final_total
