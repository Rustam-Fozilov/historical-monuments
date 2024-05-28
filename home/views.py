from django.shortcuts import render


def index(request):
    return render(request, 'apps/home/index.html')


def favorites(request):
    return render(request, 'apps/home/favorites.html')
