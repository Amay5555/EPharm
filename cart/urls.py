from django.urls import path
from . import views

urlpatterns = [
    path('' , views.viewCart, name = 'vcart'), 
    path ('<int:pk>/', views.addToCart , name= 'addtocart') ,
    path('updatecartitem/<int:pk>/', views.updateCartItem , name = 'update_cart_item'),
    path('removecartitem/<int:pk>/', views.removeCartItem , name = 'remove_cart_item'),
]