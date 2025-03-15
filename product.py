class Product:
    def _init_(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
        
    def display_info(self):
        print(f"Name: {self.name} ; Price: {self.price} ; Quantity: {self.quantity}")
        
    def update_quantity(self, new_quantity):
        self.quantity = new_quantity