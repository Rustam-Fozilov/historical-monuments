from django.contrib import messages
from django.shortcuts import render, redirect

from .models import Contact

# Create your views here.


def index(request):
    return render(request, 'apps/home/contact.html')


def send(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        message = request.POST.get('message')

        Contact.objects.create(name=name, email=email, phone=phone, message=message)
        messages.success(request, 'Xabaringiz yuborildi')
        return redirect('/contact/')
    else:
        return redirect('send')
