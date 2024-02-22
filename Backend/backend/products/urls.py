from django.urls import path
from .views import admin_product_retrieve_update_destroy, admin_product_list_create_view,product_list_view

urlpatterns = [
    # admin and staff views
    path('admin/products/', admin_product_list_create_view),
    path('admin/products/<int:pk>/', admin_product_retrieve_update_destroy),


    # regular user views
    path('products/', product_list_view),
]