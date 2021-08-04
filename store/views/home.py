from django.shortcuts import render, redirect
from store.models.category import Category
from store.models.product import Product
from django.views import View


# Create your views here.

class Index(View):

    def post(self, request):
        product = request.POST.get('product')
        remove = request.POST.get('remove')
        wishlist = request.session.get('wishlist')
        if wishlist:
            quantity = wishlist.get(product)
            if quantity:
                if remove:
                    if quantity <= 1:
                        wishlist.pop(product)
                    else:
                        wishlist[product] = quantity - 1
                else:
                    wishlist[product] = quantity + 1
            else:
                wishlist[product] = 1

        else:
            wishlist = {}
            wishlist[product] = 1

        request.session['wishlist'] = wishlist
        print('wishlist', request.session['wishlist'])
        return redirect('homepage')

    def get(self, request):
        wishlist = request.session.get('wishlist')
        if not wishlist:
            request.session['wishlist'] = {}
        products = None

        categories = Category.get_all_categories()
        categoryID = request.GET.get('category')

        if categoryID:
            products = Product.get_all_products_by_categoryid(categoryID)
        else:
            products = Product.get_all_products();
        data = {}
        data['products'] = products
        data['categories'] = categories

        print('You are ', request.session.get('email'))

        return render(request, 'index.html', data)
