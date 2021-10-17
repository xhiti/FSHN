from django.db import models


# Create your models here.
STUDY_LEVEL = (
    ("1", "bachelor"),
    ("2", "master"),
)


class ScientificBulletin(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=255, unique=True)
    description = models.TextField(max_length=500, blank=True)
    study_level = models.CharField(max_length=100, choices=STUDY_LEVEL)
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
