from django.shortcuts import render
from django.http import HttpResponse
from .models import News
from .models import Events
def index(request):
    return render(request, 'main/pages/Main.html')
def about(request):
    return render(request, 'main/pages/About.html')

def contact(request):
    return render(request, 'main/pages/Contact.html')

def events(request):
    eventss = Events.objects.all()
    return render(request, 'main/pages/Events.html', {'title': 'Our events', 'events': eventss})

def news(request):
    newss = News.objects.all()
    return render(request, 'main/pages/News.html', {'news': newss})

