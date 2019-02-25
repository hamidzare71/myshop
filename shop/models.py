from django.db import models
from django.urls import reverse

class Category(models.Model):

    name = models.CharField(max_length = 200,
            db_index = True)
    slug = models.SlugField(max_length = 200,
            unique = True)

    class Meta:
        #good for better management in admin site
        ordering = ('name',)
        verbose_name = 'Category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        '''
        rconvention for retrieve URL for given ogject(avoid path changing)

        bad way:
        <a href="/language/category/product/{{product.pk}}">Link</a>
        good way:
        <a href="{{product.get_absolute_url}}">Link</a>

        ref:https://stackoverflow.com/questions/43179875/when-to-use-django-get-absolute-url-method
        '''
        return reverse('shop:product_list_by_category', args = [self.slug])


class Product(models.Model):
    '''
    category is foreignkey to Category model, fields are:
    category,name,slug,image,descrption,price,is Available?,createTime,updateTime
    '''
    category = models.ForeignKey(Category,related_name='products', on_delete= models.CASCADE)
    name = models.CharField(max_length=200, db_index=True)
    slug=models.SlugField(max_length=200, db_index=True)
    image = models.ImageField(upload_to = 'products/%Y/%m/%d', blank =True)
    description = models.TextField(blank =True)
    price = models.DecimalField(max_digits=10,decimal_places=0) #instead of FloatField to avoid float ROUNDING :!
    available = models.BooleanField(default = True)
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)

    class Meta:
        '''
        to query sort by id,slug
        '''
        ordering = ('name',)
        index_together = (('id','slug'),)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        '''
        convention for retrieve URL for given ogject(avoid path changing)
        '''
        return reverse('shop:product_detail',args = [self.id,self.slug])

