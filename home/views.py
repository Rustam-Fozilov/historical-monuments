from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout

from monuments.models import Monument
from cities.models import Cities
from news.models import News
from .forms import RegistrationForm, LoginForm


def index(request):
    best_monuments = Monument.objects.all().order_by('?')[:4]
    cities = Cities.objects.all().order_by('?')[:3]
    news = News.objects.all().order_by('?')[:4]

    context = {
        'best_monuments': best_monuments,
        'cities': cities,
        'news': news,
    }

    return render(request, 'apps/home/index.html', context=context)


def favorites(request):
    if request.method == 'POST':
        user = request.user
        monument = Monument.objects.get(pk=request.POST['monument'])

        if user.favorites.filter(monument=monument).exists():
            user.favorites.filter(monument=monument).delete()
        else:
            user.favorites.get_or_create(monument=monument)
        return redirect(request.META.get('HTTP_REFERER'))
    else:
        user_favorites = request.user.favorites.all()
        count = request.user.favorites.count()
        context = {
            'user_favorites': user_favorites,
            'count': count
        }

        return render(request, 'apps/home/favorites.html', context=context)


def search(request):
    monuments = Monument.objects.filter(title__icontains=request.GET['query'])
    return render(request, 'apps/home/result.html', {'monuments': monuments})


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                return redirect('/')
            else:
                form.add_error('password', 'incorrect')
    else:
        form = LoginForm()
    return render(request, 'apps/auth/login.html', {'form': form})


def user_register(request):
    if request.method == "POST":
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        password = request.POST['password']
        email = request.POST['email']

        user = User.objects.create_user(first_name=first_name, last_name=last_name, email=email, password=password, username=email)
        user.save()
        login(request, user)

        return redirect('/')

    else:
        return render(request, 'apps/auth/register.html')


def user_logout(request):
    logout(request)
    return redirect('/')
