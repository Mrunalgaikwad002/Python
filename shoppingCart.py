class ShoppingCart:
    def __init__(self):
        self.items = {}

    def add_item(self, item, price):
        self.items[item] = price
        print(f"Added {item} - ₹{price}")

    def remove_item(self, item):
        if item in self.items:
            del self.items[item]
            print(f"Removed {item}")
        else:
            print("Item not found")

    def total_price(self):
        return sum(self.items.values())
    

cart = ShoppingCart()
cart.add_item("Shirt", 1200)
cart.add_item("Shoes", 2500)
cart.remove_item("Shirt")
print("Total Price:", cart.total_price())
