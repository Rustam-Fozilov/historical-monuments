from django.urls import path

from monuments import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<monument_id>/', views.show, name='show'),
]
