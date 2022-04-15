from django.shortcuts import render
from .models import About
# Create your views here.


def about(request):
    info = About.objects
    return render(request, 'about/about.html', {'info': info})