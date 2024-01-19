from django.db import models

class Artiles(models.Model):
    title = models.CharField('title', max_length=50)
    anons = models.CharField('anons', max_length=250)
    full_text = models.TextField('statya')
    date = models.DateTimeField('date of publication')

    def __str__(self):
        return self.title