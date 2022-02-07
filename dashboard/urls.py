from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('products/', views.products, name='products'),
    path('customer/<str:name>', views.customer, name='customer'),

    path('create-order/<int:pk>', views.createOrder, name='create_order'),
    path('update-order/<int:pk>', views.updateOrder, name='update_order'),
    path('delete-order/<int:pk>', views.deleteOrder, name='delete_order'),

    path("show-profile/", views.profile, name="show_profile"),

]