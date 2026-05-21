def add_item(item, cart=None):
    """Fixes the mutable default argument bug by using None as a placeholder."""
    if cart is None:
        cart = [] 
    cart.append(item)
    return cart

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
        
    # Apply discount percentage (e.g., 10% discount means paying 90% of total)
    discount_amount = raw_total * (cart["discount"] / 100)
    final_total = raw_total - discount_amount
    return final_total
def main():
    print("--- Testing Part B Fix ---")
    print(add_item("apple"))
    print(add_item("banana"))  

    print("\n--- Testing Part C: Creating Independent Carts ---")
    cart_rahul = create_cart("Rahul", discount=10) 
    cart_priya = create_cart("Priya", discount=0)  

    add_to_cart(cart_rahul, "Laptop", 55000, qty=1)
    add_to_cart(cart_rahul, "Mouse", 1500, qty=2)

    add_to_cart(cart_priya, "Books", 1200, qty=3)

    sample_tuple = (55000, "INR")
    update_price(sample_tuple, 50000)

    total_rahul = calculate_total(cart_rahul)
    total_priya = calculate_total(cart_priya)

    print(f"\n {cart_rahul['owner']}'s Cart Total (with {cart_rahul['discount']}% discount): {total_rahul:.2f} INR")
    print(f" {cart_priya['owner']}'s Cart Total (with {cart_priya['discount']}% discount): {total_priya:.2f} INR")


if __name__ == "__main__":
    main()
