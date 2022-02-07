# manage users
from typing import Callable

from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect


def allowed_users(allowed_roles: list = []) -> Callable:
    def decorator(view_func: Callable) -> Callable:
        def wrapper_func(request: HttpRequest, *args, **kwargs) -> Callable:
            print(f"Working: {allowed_roles}")
            group = None
            if request.user.groups.exists():
                group = request.user.groups.all()[0].name

            if group in allowed_roles:
                return view_func(request, *args, **kwargs)
            else:
                return HttpResponse("You Not Authorized on This Page")

        return wrapper_func

    return decorator


def admin_only(view_func: Callable):
    def wrapper_function(request: HttpRequest, *args, **kwargs) -> Callable:
        group = None
        if request.user.groups.exists():
            group = request.user.groups.all()[0].name
        if group == "customer":
            return redirect("show_profile")
        if group == "admin":
            return view_func(request, *args, **kwargs)
        else:
            return redirect('login')


    return wrapper_function
