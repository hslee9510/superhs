from django.shortcuts import render,get_object_or_404
from django.utils import timezone
from .models import Daily


def index(request):
    dailys = Daily.objects.filter(date__lte=timezone.now()).order_by('date')
    return render(request, 'blog/index.html',{'dailys':dailys})

def daily(request):
    dailys = Daily.objects.filter(date__lte=timezone.now()).order_by('date')
    return render(request, 'blog/daily_hs.html',{'dailys':dailys})

def daily_detail(request,pk):
    daily = get_object_or_404(Daily, pk=pk)
    return render(request, 'blog/daily_detail.html',{'daily':daily})

def todo(request):

    return render(request, 'blog/index.html')

def wish(request):

    return render(request, 'blog/index.html')

def inspiration(request):

    return render(request, 'blog/index.html')

def reference(request):

    return render(request, 'blog/index.html')

def trophy(request):

    return render(request, 'blog/index.html')
