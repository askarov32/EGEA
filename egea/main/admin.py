from django.contrib import admin
from .models import News
from .models import Events

admin.site.register(News)
admin.site.register(Events)