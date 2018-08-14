from django.shortcuts import render
from .models import Posths,Post


def index(request):
    return render(request, 'blog/daily_hs.html')
