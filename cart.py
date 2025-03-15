class Cart:
    def _init_(self):
        self.cart_items = []
        
    def add_items(self, product):
        self.cart_items.append(product)
        
    def calculate_total(self):
        total = 0
        for item in self.cart_items:
            total += item['price'] * item['quantity']
            return total
        
    def display_cart(self):
        for item in self.cart_items:
            print(f"Name: {item['name']}, Price: {item['price']}, Quantity: {item['quantity']}")
        