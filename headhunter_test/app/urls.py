from django.urls import path

from . import views

urlpatterns = [
    path('', views.login, name='login'),
    path('', views.questions, name='questions'),
    path('', views.results),
]
