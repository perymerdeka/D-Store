from typing import Callable
from django.http import HttpRequest
from django.shortcuts import redirect


def unauthenticated_user(view_func: Callable) -> Callable:
    def wrapper_func(request: HttpRequest, *args, **kwargs) -> Callable:
        if request.user.is_authenticated:
            return redirect('home')
        else:
            return view_func(request, *args, **kwargs)
    
    return wrapper_func


