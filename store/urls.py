#full code is self written here
from django.urls import path
from . import views


urlpatterns = [
    
    path('',views.store,name="store"),
    path('cart/',views.cart,name="cart"),
    path('checkout/',views.checkout,name="checkout"),
    path('wishlist/', views.wishlist, name="wishlist"),

]
