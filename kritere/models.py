from django.db import models


# Create your models here.
STUDY_LEVEL = (
    ("1", "bachelor"),
    ("2", "master"),
)

LAW_BASE_TYPE = (
    ("1", "law"),
    ("2", "regulation"),
    ("3", "vkm"),
    ("4", "order_and_instructions"),
    ("5", "budget"),
)


class CriteresQuotes(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=255, unique=True)
    description = models.TextField(max_length=500, blank=True)
    link = models.CharField(max_length=1000)
    study_level = models.CharField(max_length=500, choices=STUDY_LEVEL, blank=False, null=False)
    loaction = models.CharField(max_length=255, blank=False)
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


class LawBase(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=255, unique=True)
    description = models.TextField(max_length=500, blank=True)
    link = models.CharField(max_length=1000)
    law_base_type = models.CharField(max_length=500, choices=LAW_BASE_TYPE, blank=False, null=False)
    is_active = models.BooleanField(default=True)
    is_deleted = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True)
    # created_user = models.ForeignKey()
    updated_date = models.DateTimeField(auto_now=True)
    # updated_user = models.ForeignKey()

    class Meta:
        verbose_name = 'LawBase'
        verbose_name_plural = 'LawsBase'

    def __str__(self):
        return self.title
