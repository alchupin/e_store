from django.urls import path
from .views import cart_add_product, cart_detail, cart_remove_product

app_name = 'cart'

urlpatterns = [
    path('', cart_detail, name='cart_detail'),
    path('add/<int:product_id>/', cart_add_product, name='cart_add_product'),
    path('remove/<int:product_id>/', cart_remove_product, name='cart_remove_product'),
]