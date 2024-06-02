from django.urls import path

from cities import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<city_id>/', views.show, name='show'),
]
