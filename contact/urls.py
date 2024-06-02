from django.urls import path

from contact import views

urlpatterns = [
    path('', views.index, name='index'),
    path('send/', views.send, name='send'),
]
