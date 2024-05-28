from django.shortcuts import render

from monuments.models import Monument

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
    monuments = Monument.objects.all().order_by('-id')[:10]
    context = {
        'monument': monument,
        'monuments': monuments,
        'is_favorite': request.user.favorites.filter(monument=monument).exists(),
    }

    return render(request, 'apps/monuments/show.html', context=context)

