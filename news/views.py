from django.shortcuts import render

from news.models import News
from django.db.models import Q


# Create your views here.


def index(request):
    news = News.objects.all()
    context = {'news': news}

    return render(request, 'apps/news/index.html', context=context)


def show(request, news_id):
    news = News.objects.get(pk=news_id)
    context = {
        'news': news,
        'others': News.objects.filter(~Q(id=news_id)).order_by('-id')[:4]
    }

    return render(request, 'apps/news/show.html', context=context)

