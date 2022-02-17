from django.db import models
from core.models import StudyLevel


# Create your models here.
class Department(models.Model):
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
        verbose_name = 'Department'
        verbose_name_plural = 'Departments'

    def __str__(self):
        return self.title


class ScientificBulletin(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=255, unique=True)
    description = models.TextField(max_length=500, blank=True)
    study_level = models.ForeignKey(StudyLevel, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='photos/scientific_bulletin')
    link = models.CharField(max_length=1000)
    is_active = models.BooleanField(default=True)
    is_deleted = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True)
    # created_user = models.ForeignKey()
    updated_date = models.DateTimeField(auto_now=True)
    # updated_user = models.ForeignKey()

    class Meta:
        verbose_name = 'ScientificBulletin'
        verbose_name_plural = 'ScientificBulletins'

    def __str__(self):
        return self.title


class Project(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=255, unique=True)
    description = models.TextField(max_length=500, blank=True)
    image = models.ImageField(upload_to='photos/project')
    link = models.CharField(max_length=1000)
    is_active = models.BooleanField(default=True)
    is_deleted = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True)
    # created_user = models.ForeignKey()
    updated_date = models.DateTimeField(auto_now=True)
    # updated_user = models.ForeignKey()

    class Meta:
        verbose_name = 'Project'
        verbose_name_plural = 'Projects'

    def __str__(self):
        return self.title


class Doctorature(models.Model):
    author_name = models.CharField(max_length=200, blank=False, null=False)
    author_surname = models.CharField(max_length=200, blank=False, null=False)
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=255, unique=True)
    description = models.TextField(max_length=500, blank=True)
    link = models.CharField(max_length=1000)
    file = models.FileField(upload_to='doctoratures/file', blank=True)
    is_active = models.BooleanField(default=True)
    is_deleted = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    # created_user = models.ForeignKey()
    updated_date = models.DateTimeField(auto_now=True)
    # updated_user = models.ForeignKey()

    class Meta:
        verbose_name = 'Doctorature'
        verbose_name_plural = 'Doctoratures'

    def __str__(self):
        return self.title


class PublicationConference(models.Model):
    authors = models.CharField(max_length=200, blank=False, null=False)
    title = models.CharField(max_length=200, unique=True)
    conference_title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)
    description = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=255)
    finance = models.FloatField()
    link = models.CharField(max_length=1000)
    is_active = models.BooleanField(default=True)
    is_deleted = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    # created_user = models.ForeignKey()
    updated_date = models.DateTimeField(auto_now=True)
    # updated_user = models.ForeignKey()

    class Meta:
        verbose_name = 'PublicationConference'
        verbose_name_plural = 'PublicationsConferences'

    def __str__(self):
        return self.title


class LawBaseType(models.Model):
    title = models.CharField(max_length=200, unique=True)
    description = models.TextField(max_length=500, blank=True)
    is_active = models.BooleanField(default=True)
    is_deleted = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True)
    # created_user = models.ForeignKey()
    updated_date = models.DateTimeField(auto_now=True)
    # updated_user = models.ForeignKey()

    class Meta:
        verbose_name = 'LawBaseType'
        verbose_name_plural = 'LawBaseTypes'

    def __str__(self):
        return self.title


class CriterAndQuote(models.Model):
    title = models.CharField(max_length=200, unique=True)
    description = models.TextField(max_length=500, blank=True)
    link = models.CharField(max_length=1000)
    study_level = models.ForeignKey(StudyLevel, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)
    is_deleted = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True)
    # created_user = models.ForeignKey()
    updated_date = models.DateTimeField(auto_now=True)
    # updated_user = models.ForeignKey()

    class Meta:
        verbose_name = 'CriterAndQuote'
        verbose_name_plural = 'CriteresAndQuotes'

    def __str__(self):
        return self.title


class LawBase(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=255, unique=True)
    description = models.TextField(max_length=500, blank=True)
    link = models.CharField(max_length=1000)
    law_base_type = models.ForeignKey(LawBaseType, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)
    is_deleted = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True)
    # created_user = models.ForeignKey()
    updated_date = models.DateTimeField(auto_now=True)
    # updated_user = models.ForeignKey()

    class Meta:
        verbose_name = 'LawBase'
        verbose_name_plural = 'LawBases'

    def __str__(self):
        return self.title


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
