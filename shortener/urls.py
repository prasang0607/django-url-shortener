from django.urls import path
from shortener.views import index, redirect_to

urlpatterns = [
    path('', index, name='index'),
    path('<str:short_code>/', redirect_to),
]
