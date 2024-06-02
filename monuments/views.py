from django.shortcuts import render

from monuments.models import Monument
from django.db.models import Q

# Create your views here.


def index(request):
    monuments = Monument.objects.all()
    context = {
        'monuments': monuments,
        'count': Monument.objects.count()
    }

    return render(request, 'apps/monuments/index.html', context=context)


def show(request, monument_id: str):
    monument = Monument.objects.get(pk=monument_id)
    monuments = Monument.objects.filter(~Q(id=monument_id)).order_by('-id')[:10]

    is_favorite = False
    if request.user.is_authenticated:
        is_favorite = request.user.favorites.filter(monument=monument).exists()

    context = {
        'monument': monument,
        'monuments': monuments,
        'is_favorite': is_favorite,
    }

    return render(request, 'apps/monuments/show.html', context=context)

