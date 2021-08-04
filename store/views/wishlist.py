from django.views import View
from django.shortcuts import render, redirect

from store.models.customer import Customer

from django.contrib.auth.hashers import check_password
from store.models.product import Product
from store.models.wishlist import Wishlist


class Wishlist(View):

    def get(self, request):
        ids = list(request.session.get('wishlist').keys())
        products = Product.get_product_by_id(ids)
        print(products)
        #Wishlist.objects.create(owner=request.user, product_id=ids)
        return render(request, 'wishlist.html', {'products': products})
