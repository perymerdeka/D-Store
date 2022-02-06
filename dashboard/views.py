from django.http import HttpRequest
from django.shortcuts import render, redirect
from django.forms import inlineformset_factory
from django.contrib.auth.decorators import login_required


from .decorators import admin_only, allowed_users

from .forms import OrderForm
from .filters import OrderFilter

from .models import *

# Create your views here.


@login_required(login_url="login")
@admin_only
def home(request):
    orders = Order.objects.all()
    customers = Customer.objects.all()

    # sum the product
    total_order = orders.count()
    total_customer = customers.count()
    delivered = orders.filter(status="Delivered").count()
    pending = orders.filter(status="Pending").count()

    context: dict = {
        "orders": orders,
        "customers": customers,
        "total_order": total_order,
        "total_customer": total_customer,
        "delivered": delivered,
        "pending": pending,
    }

    return render(request, "dashboard/dashboard.html", context=context)


@login_required(login_url="login")
@allowed_users(allowed_roles=['admin'])
def products(request):
    products = Product.objects.all()
    context: dict = {"products": products}
    return render(request, "dashboard/products.html", context=context)


@login_required(login_url="login")
@allowed_users(allowed_roles=['admin'])
def customer(request, name):
    customer = Customer.objects.get(name=name)
    orders = customer.order_set.all()
    total_order = orders.count()

    # filter
    customerFilter = OrderFilter(request.GET, queryset=orders)

    # queryset
    orders = customerFilter.qs

    context: dict = {
        "customer": customer,
        "orders": orders,
        "total_order": total_order,
        "customerFilter": customerFilter,
    }
    return render(request, "dashboard/customer.html", context=context)


# CRUD Operations
@login_required(login_url="login")
def createOrder(request, pk):
    OrderFormSet = inlineformset_factory(Customer, Order, fields=("product", "status"))
    customer = Customer.objects.get(id=pk)
    # form = OrderForm(initial={'customer': customer})
    formset = OrderFormSet(queryset=Order.objects.none(), instance=customer)
    if request.method == "POST":
        formset = OrderFormSet(request.POST, instance=customer)
        if formset.is_valid():
            formset.save()
            return redirect("home")

    context: dict = {"formset": formset}
    return render(request, "dashboard/forms/createOrder.html", context=context)


@login_required(login_url="login")
@allowed_users(allowed_roles=['admin'])
def updateOrder(request, pk: int):
    order = Order.objects.get(id=pk)
    form = OrderForm(instance=order)
    if request.method == "POST":
        form = OrderForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            return redirect("home")

    context: dict = {"order": order, "form": form}
    return render(request, "dashboard/forms/createOrder.html", context=context)


@login_required(login_url="login")
@allowed_users(allowed_roles=['admin'])
def deleteOrder(request, pk: int):
    order = Order.objects.get(id=pk)
    if request.method == "POST":
        order.delete()
        return redirect("home")

    context: dict = {"item": order}
    return render(request, "dashboard/partials/delete.html", context=context)
