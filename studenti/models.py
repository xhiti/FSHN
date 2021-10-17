from django.db import models


# Create your models here.
class Burse(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=255, unique=True)
    description = models.TextField(max_length=500, blank=True)
    link = models.CharField(max_length=1000)
    is_active = models.BooleanField(default=True)
    is_deleted = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True)
    # created_user = models.ForeignKey()
    updated_date = models.DateTimeField(auto_now=True)
    # updated_user = models.ForeignKey()

    class Meta:
        verbose_name = 'Burse'
        verbose_name_plural = 'Burses'

    def __str__(self):
        return self.title


class Notification(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=255, unique=True)
    description = models.TextField(max_length=1000, blank=True)
    link = models.CharField(max_length=1000)
    reference = models.CharField(max_length=255, blank=True)
    is_pinned = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_deleted = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True)
    # created_user = models.ForeignKey()
    updated_date = models.DateTimeField(auto_now=True)
    # updated_user = models.ForeignKey()

    class Meta:
        verbose_name = 'Notification'
        verbose_name_plural = 'Notifications'

    def __str__(self):
        return self.title
