from django.urls import path

from news import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<news_id>/', views.show, name='show'),
]
