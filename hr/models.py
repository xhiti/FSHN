from django.db import models
from faculty.models import Department
from core.models import Program, Course, StudyLevel


# Create your models here.
class AcademicTitle(models.Model):
    code = models.CharField(max_length=12, unique=True)
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    is_active = models.BooleanField(default=True)
    is_deleted = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True)
    # created_user = models.ForeignKey()
    updated_date = models.DateTimeField(auto_now=True)
    # updated_user = models.ForeignKey()

    class Meta:
        verbose_name = 'AcademicTitle'
        verbose_name_plural = 'AcademicTitles'

    def __str__(self):
        return self.title


class Academic(models.Model):
    nid = models.CharField(max_length=12, unique=True)
    name = models.CharField(max_length=200)
    surname = models.CharField(max_length=200)
    email = models.EmailField(max_length=255)
    phone = models.CharField(max_length=15)
    office = models.CharField(max_length=100)
    image = models.ImageField(upload_to='photos/academic')
    slug = models.SlugField(max_length=255, unique=True)
    description = models.TextField(max_length=500, blank=True)
    link = models.CharField(max_length=1000)
    bio = models.CharField(max_length=1000)
    education = models.CharField(max_length=1000)
    academic_title = models.ForeignKey(AcademicTitle, on_delete=models.CASCADE)
    courses = models.OneToOneField(Course, on_delete=models.CASCADE)
    science_article = models.CharField(max_length=1000)
    scientific_research = models.CharField(max_length=1000)
    activities = models.CharField(max_length=1000)
    social_links = models.CharField(max_length=255)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)
    is_deleted = models.BooleanField(default=False)
    joined_date = models.DateTimeField(),
    left_date = models.DateTimeField()
    created_date = models.DateTimeField(auto_now_add=True)
    # created_user = models.ForeignKey()
    updated_date = models.DateTimeField(auto_now=True)
    # updated_user = models.ForeignKey()

    class Meta:
        verbose_name = 'Academic'
        verbose_name_plural = 'Academics'

    def __str__(self):
        return self.name


class Student(models.Model):
    nid = models.CharField(max_length=12, unique=True)
    name = models.CharField(max_length=200)
    father_name = models.CharField(max_length=200)
    surname = models.CharField(max_length=200)
    email = models.EmailField(max_length=255)
    program = models.ForeignKey(Program, on_delete=models.CASCADE)
    year_of_study = models.IntegerField()
    group = models.CharField(max_length=5)
    slug = models.SlugField(max_length=255, unique=True)
    description = models.TextField(max_length=500, blank=True)
    link = models.CharField(max_length=1000)
    study_level = models.ForeignKey(StudyLevel, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)
    is_deleted = models.BooleanField(default=False)
    joined_date = models.DateTimeField(),
    left_date = models.DateTimeField()
    created_date = models.DateTimeField(auto_now_add=True)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    # created_user = models.ForeignKey()
    updated_date = models.DateTimeField(auto_now=True)
    # updated_user = models.ForeignKey()

    class Meta:
        verbose_name = 'Student'
        verbose_name_plural = 'Students'

    def __str__(self):
        return self.name


class Admin(models.Model):
    name = models.CharField(max_length=200)
    surname = models.CharField(max_length=200)
    email = models.EmailField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)
    is_active = models.BooleanField(default=True)
    is_deleted = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True)
    is_admin = models.BooleanField(default=True)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    is_superadmin = models.BooleanField(default=False)
    # created_user = models.ForeignKey()
    updated_date = models.DateTimeField(auto_now=True)
    # updated_user = models.ForeignKey()

    class Meta:
        verbose_name = 'Admin'
        verbose_name_plural = 'Admins'

    def __str__(self):
        return self.name
