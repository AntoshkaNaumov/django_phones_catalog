from django.shortcuts import render, redirect
from phones.models import Phone


def index(request):
    return redirect('catalog')


def show_catalog(request):
    template = 'catalog.html'
    phone_objects = Phone.objects.all()
    sort_pages = request.GET.get('sort')

    # сортировка каталога по цене
    if sort_pages == 'max_price':
        phone_objects = phone_objects.order_by('price').reverse()
    elif sort_pages == 'min_price':
        phone_objects = phone_objects.order_by('price')
    elif sort_pages == 'name':
        # сортировка каталога по названию
        phone_objects = phone_objects.order_by('name')

    context = {'phones': phone_objects}
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    phone = Phone.objects.get(slug=slug)
    context = {'phone': phone}
    return render(request, template, context)
