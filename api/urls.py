from django.urls import path

from . import views

urlpatterns = [
    path('calculate/', views.CalculateBmiAPIView.as_view(), name='bmi-api'),
]
