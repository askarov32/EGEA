from django.db import models

class News(models.Model):
    title = models.CharField('Title', max_length=50)
    news = models.TextField('News for today')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'News'
        verbose_name_plural = 'News'

class Events(models.Model):
    title = models.CharField('Title', max_length=50)
    events = models.TextField('Events')
    images = models.ImageField('Images')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Event'
        verbose_name_plural ='Events'
