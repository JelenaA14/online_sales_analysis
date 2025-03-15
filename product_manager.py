class ProductManager:
    def _init_(self):
        self.product = []
            
    def add_products(self, product):
        self.products.append(product)
        
    def display_products(self):
        for product in self.products:
            product.display_info()
            
    def calculate_total_value(self):
        total_value = 0
        for product in self.products:
            total_value += product.price * product.quantity
            return total_value
        
    def remove_product(self, product_name):
        self.products = [product for product in self.products if product.name != product_name]       