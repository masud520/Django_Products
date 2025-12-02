from django.shortcuts import render, redirect
from .models import Product, Category

def product_list(request):
    products = Product.objects.all()
    return render(request, 'products/product_list.html', {'products': products})

def add_product(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        price = request.POST.get('price')
        category_id = request.POST.get('category')
        description = request.POST.get('description')
        image = request.FILES.get('image')
        category = Category.objects.get(id=category_id)
        Product.objects.create(name=name, price=price, category=category, description=description, image=image)
        return redirect('product_list')
    categories = Category.objects.all()
    return render(request, 'products/add_product.html', {'categories': categories})

def product_detail(request, id):
    product = Product.objects.get(id=id)
    return render(request, 'products/product_detail.html', {'product': product})
