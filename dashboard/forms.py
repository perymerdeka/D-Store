from django.forms import ModelForm

from .models import Customer, Order

class CustomerForm(ModelForm):
    class Meta:
        model = Customer
        fields: str = '__all__'
        exclude: list = ['user']

class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = '__all__'
