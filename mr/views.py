from django.shortcuts import render

from .models import newsIndex

def index(request):
    newss = newsIndex.objects.all()
    return render(request, 'mr/index.html', context={'newss': newss})
