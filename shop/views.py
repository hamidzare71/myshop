from django.shortcuts import render, get_object_or_404
from .models import Category,Product
from cart.forms import CartAddProductForm


def product_list(request,category_slug=None):
#     list all products or filter products by given category

#     category = None #no needed any more
    categories = Category.objects.all()

#   filter queries to products that available
    products = Product.objects.filter(available = True)

    if category_slug:   #optionally we filter product by category
        category =get_object_or_404(Category,slug=category_slug)
        products = products.filter(category=category)

    return render(request,
            'shop/product/list.html',
            {
#                 'category':category,
                'categories':categories,
                'products':products
            })

def product_detail(request,id,slug):
#     display single prdct
    product = get_object_or_404(Product,
            id = id, #match id given instance or say not found
            slug = slug,
            available = True)

    cart_product_form = CartAddProductForm()

    return render(request,
            'shop/product/detail.html',
            {'product':product,
                'cart_product_form':cart_product_form})


