from django.shortcuts import render
def index(request):
    return render(request, 'main/pages/Main.html')
def about(request):
    return render(request, 'main/pages/About.html')

def contact(request):
    return render(request, 'main/pages/Contact.html')

def events(request):
    return render(request, 'main/pages/Events.html', {'title': 'Our events', 'events': eventss})

def news(request):
    return render(request, 'main/pages/News.html', {'news': newss})

