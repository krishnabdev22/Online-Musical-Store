from django import template

register = template.Library()

@register.filter(name='is_in_wishlist')
def is_in_wishlist(product , wishlist):
    keys = wishlist.keys()
    for id in keys:
        if int(id) == product.id:
            return True
    return False;


@register.filter(name='wishlist_quantity')
def wishlist_quantity(product , wishlist):
    keys = wishlist.keys()
    for id in keys:
        if int(id) == product.id:
            return wishlist.get(id)

    return 0;

@register.filter(name='price_total')
def price_total(product , wishlist):
    return product.price * wishlist_quantity(product, wishlist)


@register.filter(name='total_wishlist_price')
def total_wishlist_price(products , wishlist):
    sum = 0;
    for p in products:
        sum += price_total(p , wishlist)

    return sum
