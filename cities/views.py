from django.shortcuts import render

from cities.models import Cities
from django.db.models import Q


# Create your views here.


def index(request):
    cities = Cities.objects.all()
    context = {
        'cities': cities,
        'count': Cities.objects.count(),
    }

    return render(request, 'apps/cities/index.html', context=context)


def show(request, city_id):
    cities = Cities.objects.get(pk=city_id)
    context = {
        'city': cities,
        # not equal for this ID
        'other': Cities.objects.filter(~Q(id=city_id)).order_by('-id')[:10]
    }

    return render(request, 'apps/cities/show.html', context=context)
