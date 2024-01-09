from django.shortcuts import render, redirect

from phones.models import Phone


def index(request):
    return redirect('catalog')


def show_catalog(request):
    template = 'catalog.html'
    r = request.GET.get('sort')
    if r == 'min_price':
        a = Phone.objects.all().order_by('price')
    elif r == 'max_price':
        a = Phone.objects.all().order_by('-price')
    elif r == 'name':
        a = Phone.objects.all().order_by('name')
    else:
        a = Phone.objects.all()
    context = {'phones': a}
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    a = Phone.objects.get(slug=slug)
    context = {'phone': a}
    return render(request, template, context)