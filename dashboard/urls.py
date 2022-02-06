from django.urls import path

from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('products/', products, name='products'),
    path('customer/<str:name>', customer, name='customer'),

    path('create-order/<int:pk>', createOrder, name='create_order'),
    path('update-order/<int:pk>', updateOrder, name='update_order'),
    path('delete-order/<int:pk>', deleteOrder, name='delete_order'),

]