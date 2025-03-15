from product_manager import ProductManager
from cart import Cart
import random

if __name__ == "_main_":
    manager = ProductManager()
    
    manager.add_products("Laptop", 1200, 5)
    manager.add_products("Headphones", 400, 10)
    manager.add_products("Phone", 950, 6)
    
    print("List of product:"), manager.display_products()
    
    total_value = manager.calculate_total_value()
    print(f"The total value: {total_value}")

    cart = Cart()

    for _ in range(3):
       random_product = random.choice(manager.products)
    
    cart.add_items(random_product)
    print ("Basket contents"), cart.display_cart()

    total_cart_value = cart.calculate_total()
    print(f"Total cart value: {total_cart_value}")
