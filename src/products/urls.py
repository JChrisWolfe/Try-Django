from django.urls import path
# We are going to do a Dynamic URL Routing
# Refer to: https://www.youtube.com/watch?v=zlvX0Rb1Wl0&list=PLEsfXFp6DpzTD1BD1aWNxS2Ep06vIkaeW&index=29
#  or 'Try DJANGO Tutorial - 29' - Dynamic URL Routing on Youtube 
from .views import (
    product_create_view, 
    product_detail_view, 
    product_delete_view,
    product_list_view,
    product_update_view,
    
)

app_name = 'products' # Refer to 'Try DJANGO Tutorial - 35 - In App URLs and Namespacing', and products/models.py.
urlpatterns = [
    path('', product_list_view, name='product-list'),
    path('create/', product_create_view, name='product-list'), # What's the name param for? Check 'products/models.py' and it's get_absolute_url method.
    path('<int:id>/', product_detail_view, name='product-detail'), #http://127.0.0.1/product/1, /product/2, etc. <int:id> = Some ID number in DB.
    path('<int:id>/update/', product_update_view, name='product-update'),#http://127.0.0.1:8000/product/<int:id>/update
    path('<int:id>/delete/', product_delete_view, name='product-delete'),#http://127.0.0.1:8000/product/<int:id>/delete
]