from django.shortcuts import render
from django.shortcuts import redirect


# Create your views here.

def home_view(request):
    context = {} 
    return render(request, "app1/home.html", context)


def signup_view(request):
    context = {} 
    return render(request, "app1/createAccount.html", context)

def login_view(request):
    context = {} 
    return render(request, "app1/login.html", context)    


