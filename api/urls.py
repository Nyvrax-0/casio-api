from django.urls import path
from .views import (
    product_list, api_root, get_cart, 
    add_to_cart, remove_from_cart, clear_cart
)

urlpatterns = [
    path('', api_root),
    path('products/', product_list),
    path('cart/', get_cart),
    path('cart/add/<int:product_id>/', add_to_cart),
    path('cart/remove/<int:product_id>/', remove_from_cart),
    path('cart/clear/', clear_cart),
]