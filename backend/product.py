class Product:
    def __init__(self, product_id, name, category, price, stock, description):
        self.product_id = product_id
        self.name = name
        self.category = category
        self.price = price
        self.stock = stock
        self.description = description

    def display(self):
        print(
            self.product_id,
            self.name,
            self.category,
            self.price,
            self.stock
        )

class ProductManager:

    def add_product(self):
        pass

    def show_products(self):
        pass

    def search_product(self):
        pass

    def update_product(self):
        pass

    def delete_product(self):
        pass