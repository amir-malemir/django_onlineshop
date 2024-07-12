from products.models import Products
from django.contrib import messages
from django.utils.translation import gettext as _


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

    def add(self, product, quantity=1, replace_current_quantity=False):
        """
            add the specified product to the cart if it exists
        """
        product_id = str(product.id)

        if product_id not in self.cart:
            self.cart[product_id] = {'quantity': 0}

        if replace_current_quantity:
            self.cart[product_id]['quantity'] = quantity

        else:
            self.cart[product_id]['quantity'] += quantity

        messages.success(self.request, _('Product Successfully Added To Cart'))
        self.save()

    def remove(self, product):
        """ remove a product from the cart """
        product_id = str(product.id)

        if product_id in self.cart:
            del self.cart[product_id]
            messages.warning(self.request, _('Product Successfully Removed'))
            self.save()

    def save(self):
        """ mark session as modified to save changes """
        self.session.modified = True

    def __iter__(self):
        product_ids = self.cart.keys()
        products = Products.objects.filter(id__in=product_ids)

        cart = self.cart.copy()

        for product in products:
            cart[str(product.id)]['product_obj'] = product

        for item in cart.values():
            item['total_price'] = item['product_obj'].price * item['quantity']
            yield item

    def __len__(self):
        return sum(item['quantity'] for item in self.cart.values())

    def clear(self):
        del self.session['cart']
        self.save()

    def get_total_price(self):
        product_ids = self.cart.keys()
        return sum(item['quantity'] * item['product_obj'].price for item in self.cart.values())
