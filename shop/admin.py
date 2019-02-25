# here is administration site config, where the registerd models and details show
from django.contrib import admin
from shop.models import Category,Product

@admin.register(Category)
# decorator for display category in admin site
class CategoryAdmin(admin.ModelAdmin):

    list_display = ['name','slug']  #display name,slug in list_display page
    prepopulated_fields = {'slug': ('name',)} #automatic filling slug when name entering


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
#     this class config product page
    list_display = ['name','slug','price',
            'available','created','updated']
    list_filter = ['available','created','updated']
    list_editable = ['price','available']   #you can edit them in list_display image
    prepopulated_fields = {'slug':('name',)}
