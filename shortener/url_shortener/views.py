from rest_framework import generics
from .models import ShortURL
from .serializers import ShortURLSerializer
from django.shortcuts import get_object_or_404, redirect
from .models import ShortURL

class ShortURLCreateAPIView(generics.CreateAPIView):
    queryset = ShortURL.objects.all()
    serializer_class = ShortURLSerializer


def redirect_view(request, short_code):
    url = get_object_or_404(ShortURL, short_code=short_code)
    return redirect(url.original_url)