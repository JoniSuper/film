from django.shortcuts import render

from .models import newsIndex

def index(request):
    news = newsIndex.objects.all()
    return render(request, 'mr/index.html', {'news': news})
