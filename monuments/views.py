from django.shortcuts import render

from monuments.models import Monument

# Create your views here.


def index(request):
    return render(request, 'apps/monuments/index.html')


def show(request, monument_id: str):
    # monument = Monument.objects.get(pk=monument_id)
    # context = {'monument': monument}

    return render(request, 'apps/monuments/show.html')

