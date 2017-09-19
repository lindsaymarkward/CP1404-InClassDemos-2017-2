class Product:
    """"""
    def __init__(self, name='', price=0.0, is_onsale=False):
        self.name = name
        self.price = price
        self.is_onsale = is_onsale

    def __str__(self):
        return "{} ${:.2f} ({})".format(self.name, self.price, self.is_onsale)

    def put_on_sale(self, discount_percentage):
        """Put product on sale by reducing price by discount_percentage."""
        self.is_onsale = True
        self.price *= (1 - discount_percentage)

if __name__ == '__main__':

    thing = Product()
    # print(thing)

    phone = Product("Phone", 340, False)
    # print(phone)
    # print(phone.price)

    products = [Product("Phone", 340, False),
                Product("PC", 1420.95, False),
                Product("Plant", 24.5, True),
                Product('Bottle', 420.95, True)]

    # for product in products:
    #     print(product.name)

    on_sale_products = [product for product in products if product.is_onsale]
    print(on_sale_products)
    print([str(product) for product in on_sale_products])

    # for product in on_sale_products:
    #     print(product.name)

    print(phone)
    phone.put_on_sale(0.1)
    print(phone)
