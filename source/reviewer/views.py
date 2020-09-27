from django.shortcuts import redirect, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Product, Review
from .forms import ProductForm, ReviewForm, SimpleSearchForm
from django.db.models import Q

class IndexView(ListView):
    template_name = 'products/index.html'
    context_object_name = 'products'

    def get_context_data(self, *, object_list=None, **kwargs):
        form = SimpleSearchForm(data=self.request.GET)
        if form.is_valid():
            search = form.cleaned_data['search']
            kwargs['search'] = search
        return super().get_context_data(object_list=object_list, **kwargs)

    def get_queryset(self):
        data = Product.objects.all()
        form = SimpleSearchForm(data=self.request.GET)
        if form.is_valid():
            search = form.cleaned_data['search']
            if search:
                data = data.filter(Q(product_name__icontains=search) | Q(category__icontains=search))
        return data


class ProductView(TemplateView):
    template_name = 'products/product_view.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pk = self.kwargs.get('pk')
        product = get_object_or_404(Product, pk=pk)
        context['product'] = product
        return context


class ProductEditView(UpdateView):
    template_name = 'products/product_edit.html'
    form_class = ProductForm
    model = Product

    def get_success_url(self):
        return reverse('product_view', kwargs={'pk': self.object.pk})


class ProductRemoveView(DeleteView):
    template_name = 'products/product_remove.html'
    model = Product
    success_url = reverse_lazy('index')

    def get(self, request, *args, **kwargs):
        return self.delete(request, *args, **kwargs)


class ProductCreateView(CreateView):
    template_name = 'products/product_add.html'
    model = Product
    form_class = ProductForm

    def get_success_url(self):
        return reverse('product_view', kwargs={'pk': self.object.pk})


class ReviewListView(ListView):
    template_name = 'reviews/review_list_view.html'
    context_object_name = 'reviews'
    model = Review


class ReviewDetailView(DetailView):
    template_name = 'reviews/review_detail.html'
    model = Review


class ReviewCreateView(CreateView):
    template_name = 'reviews/review_create.html'
    model = Review
    form_class = ReviewForm

    def get_success_url(self):
        return reverse('review_detail', kwargs={'pk': self.object.pk})


class ReviewEditView(UpdateView):
    template_name = 'reviews/review_edit.html'
    form_class = ReviewForm
    model = Review

    def get_success_url(self):
        return reverse('review_detail', kwargs={'pk': self.object.pk})


class ReviewDeleteView(DeleteView):
    template_name = 'reviews/review_delete.html'
    model = Review
    success_url = reverse_lazy('index')

    def get(self, request, *args, **kwargs):
        return self.delete(request, *args, **kwargs)

