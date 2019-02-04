'''
URL patterns for product catalog and views we defined in views.py
'''
from django.urls import path
from . import views


app_name = 'shop'

urlpatterns = [
        path('',views.product_list,name = 'product_list'),
        path('<slug:category_slug>/',views.product_list,
            name='product_list_by_category'),

#also slug in Url helps us to have urs frndly SEO for products
        path('<int:id>/<slug:slug>/',views.product_detail,
            name= 'product_detail'),
]
