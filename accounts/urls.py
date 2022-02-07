from django.urls import path

from . import views

urlpatterns = [
    path("login/", views.loginPage, name="login"),
    path("register/", views.registerPage, name="register"),
    path("logout/", views.logoutUser, name="logout"),
    path('settings', views.accountSettings, name='accounts_settings')
    
]
