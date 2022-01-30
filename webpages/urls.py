from django.urls import path

from . import views

urlpatterns = [
    path('', views.IndexPageView.as_view(), name='index'),
    path('about/', views.AboutPageView.as_view(), name='about'),
]
