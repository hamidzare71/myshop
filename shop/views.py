from django.shortcuts import render, get_object_or_404
from .models import Category,Product
from cart.forms import CartAddProductForm


def product_list(request,category_slug=None):
    '''
    list all products or filter products by given category
    '''
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available = True) #filter queries to products that available
    if category_slug:   #optionally we filter product by category
        category =get_object_or_404(Category,slug=category_slug)
        products = products.filter(category=category)
    return render(request,
            'shop/product/list.html',
            {'category':category,
                'categories':categories,
                'products':products})
            #Oh!,what was the render duty in this view?
    #ok, later on :)

def product_detail(request,id,slug):
    '''
    display single prdct 
    '''
    product = get_object_or_404(Product,
            id = id,
            slug = slug,
            available = True)    #match id given instance or say not found :(

    cart_product_form = CartAddProductForm()

    return render(request,
            'shop/product/detail.html',
            {'product':product,
                'cart_product_form':cart_product_form})


