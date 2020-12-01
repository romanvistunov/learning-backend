from django.shortcuts import render, get_object_or_404
from system.models import Category, Product, Subcategory
from django.db.models import Q


def index(request):
    categories = Category.objects.all()
    products = Product.objects.all()
    context = {'products': products, 'categories': categories}
    template = 'index.html'
    return render(request, template, context)


def global_search(request):
    categories = Category.objects.all()
    query = request.GET.get('text')
    search_results = Product.objects.filter(Q(name__icontains=query))
    context = {'search_results':search_results, 'categories': categories}
    template = 'index.html'
    return render(request, template, context)


def product_list_by_category(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.all()
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    template = 'index.html'
    context = {'category': category, 'categories': categories, 'products': products,}
    return render(request, template, context)


def product_list_by_subcategory(request, category_slug=None, subcategory_slug=None):
    category = None
    subcategory = None
    categories = Category.objects.all()
    products = Product.objects.all()
    if subcategory_slug:
        category = get_object_or_404(Category, slug=category_slug)
        subcategory = get_object_or_404(Subcategory, slug=subcategory_slug)
        products = products.filter(category=category, subcategory=subcategory)

    template = 'index.html'
    context = {'category': category, 'categories': categories, 'products': products,}
    return render(request, template, context)