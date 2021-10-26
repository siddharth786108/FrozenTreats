from django.contrib.auth.models import User,auth
from django.shortcuts import render,redirect
from .models import submit

# Create your views here.
def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')


def services(request):
    return render(request, 'services.html')


def contact(request):
    return render(request, 'contact.html')


def order(request):
    return render(request, 'order.html')


def submit(request):
    if request.method == "POST":
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        email = request.POST.get('email')
        address = request.POST.get('address')
        phone = request.POST.get('phone')
        Submit=submit(firstname=firstname, lastname=lastname, email=email, address=address, phone=phone)
        Submit.save()
    return render(request, 'order.html')


def payment(request):
    return render(request, 'payment.html')


def Chocolate(request):
    return render(request, 'Chocolate.html')


def small_pack(request):
    return render(request, 'small_pack.html')


def family_pack(request):
    return render(request, 'family_pack.html')
