from django.shortcuts import render

# Create your views here.


def login_page(request):
    return render(request, "core/login.html")


def dashboard(request):

    return render(request, "core/dashboard.html")
