

class Cart:
    def __init__(self, request):
        """
        initialize the cart object
        """
        self.request = request

        self.session = self.request.session

        cart = self.session.get('cart')

        if not cart:
            cart = self.session['cart'] = {}

        self.cart = cart

    def add(self, product, quantity=1):
        """
            add the specified product to the cart if it exists
        """
        product_id = str(product.id)

        if product_id not in self.cart:
            self.cart[product_id] = {'quantity': quantity}

        else:
            self.cart[product_id]['quantity'] += quantity
        self.save()

    def remove(self, product):
        """ remove a product from the cart """
        product_id = str(product.id)

        if product_id in self.cart:
            del self.cart[product_id]
            self.save()

    def save(self):
        """ mark session as modified to save changes """
        self.session.modified = True

