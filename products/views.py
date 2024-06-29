from django.views import generic
from django.shortcuts import get_object_or_404, render
from django.contrib import messages

from .models import Products, Comments
from .forms import CommentForm


def test_messages(request):
    messages.success(request, 'Success Message')
    messages.warning(request, 'Alert Message')
    messages.error(request, 'Error Message')
    return render(request, 'products/test.html')


class ProductListView(generic.ListView):
    # model = Products
    queryset = Products.objects.filter(active=True)
    template_name = 'products/product_list.html'
    context_object_name = 'products'


class ProductDetailView(generic.DetailView):
    model = Products
    template_name = "products/product_detail.html"
    context_object_name = 'product'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comment_form'] = CommentForm()
        return context


class CommentCreateView(generic.CreateView):
    model = Comments
    form_class = CommentForm

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.author = self.request.user
        product_id = int(self.kwargs['pk'])
        product = get_object_or_404(Products, id=product_id)

        obj.product = product
        return super().form_valid(form)

