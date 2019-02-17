from decimal import Decimal
from django.conf import settings
from shop.models import Product

class Cart(object):
    '''
    here we add,update,remove,iterate,clean,len(cart items) and get price and costs
    '''


    def __init__(self, request):
        '''
        init the cart.
        '''
        self.session = request.session  #store current session to accesible to another methods
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            #             save an empty cart in session        
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart



    #method4
    def add(self,product,quantity = 1, update_quantity = False):
        '''
        add product to the cart or update its quantity
        '''
        product_id  = str(product.id)
        if product_id not in self.cart:
            self.cart[product_id] = {'quantity': 0,'price':str(product.price)} #str because of serialize it
        if update_quantity:
            self.cart[product_id]['quantity'] = quantity
        else:
            self.cart[product_id]['quantity'] += quantity
        self.save()



    #method5
    def save(self):
        #make the session as 'modified' and need to save
        self.session.modified = True



    def remove(self, product):
        '''
        remove cart products
        '''

        product_id = str(product.id)
        if product_id in self.cart:
            del self.cart[product_id]
            self.save()



    #method2
    def __iter__(self):
        '''
        iterate items in cart from DB, return amounts of
        items and total_price of each item
        '''
        product_ids = self.cart.keys()
        products = Product.objects.filter(id__in = product_ids)

        cart = self.cart.copy()
        for product in products:
            cart[str(product.id)]['product'] = product

        for item in cart.values():
            item['price'] = Decimal(item['price'])
            item['total_price'] = item['price']* item['quantity']
            yield item



    #method3
    def __len__(self):
        '''
        count all items in cart
        '''
        #here we use 'Generator Expression that is similar to comprehension
        return sum(item['quantity'] for item in self.cart.values())



    def get_total_price(self):
        '''
        get cost of all items
        '''
#         return sum(item['total_price'] for item in self.cart.values()
        return sum(Decimal(item['price']) * item['quantity'] for item in self.cart.values())



    def clear(self):
        # remove cart from session
        del self.session[settings.CART_SESSION_ID]
        self.save()

