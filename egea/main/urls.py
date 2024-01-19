from django.urls import path
from . import views
urlpatterns = [
    path('', views.index),
    path('About.html', views.about),
    path('Contact.html', views.contact),
    path('Events.html', views.events),
    path('News.html', views.news),
    path('Main.html', views.index)
]
