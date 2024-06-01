from django.views import generic

from .models import Products


class ProductListView(generic.ListView):
    # model = Products
    queryset = Products.objects.filter(active=True)
    template_name = 'products/product_list.html'
    context_object_name = 'products'
