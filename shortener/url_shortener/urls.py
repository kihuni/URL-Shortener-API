from django.urls import path
from .views import ShortURLCreateAPIView, redirect_view

urlpatterns = [
    path('api/shorten/', ShortURLCreateAPIView.as_view(), name='shorten-url'),
    path('<str:short_code>/', redirect_view, name='redirect-url'),
]
