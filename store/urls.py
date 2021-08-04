from django.urls import path
from .views.login import Login, logout
from .views.signup import Signup
from .views.home import Index
from .views.wishlist import Wishlist



urlpatterns = [
    path('', Index.as_view(), name='homepage'),
    path('signup', Signup.as_view(), name='signup'),
    path('login', Login.as_view(), name='login'),
    path('logout', logout, name='logout'),
    path('wishlist', Wishlist.as_view(), name='wishlist')
]
