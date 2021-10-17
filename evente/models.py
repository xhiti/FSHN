from django.db import models


# Create your models here.
class Event(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=255, unique=True)
    description = models.TextField(max_length=500, blank=True)
    image = models.ImageField(upload_to='photos/event')
    link = models.CharField(max_length=1000)
    location = models.CharField(max_length=255, blank=False)
    is_active = models.BooleanField(default=True)
    is_deleted = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True)
    # created_user = models.ForeignKey()
    updated_date = models.DateTimeField(auto_now=True)
    # updated_user = models.ForeignKey()

    class Meta:
        verbose_name = 'Event'
        verbose_name_plural = 'Events'

    def __str__(self):
        return self.title
