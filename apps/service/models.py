from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from apps.common.models import BaseModel


class Question(BaseModel):
    name = models.CharField(max_length=100)


    class Meta:
        verbose_name = 'Question'
        verbose_name_plural = 'Questions'

    def __str__(self):
        return self.name


class FAQ(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer = models.TextField()

    class Meta:
        verbose_name = 'FAQ'
        verbose_name_plural = 'FAQs'

    def __str__(self):
        return self.question


class Region(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'Region'
        verbose_name_plural = 'Regions'

    def __str__(self):
        return self.name


class EducationName(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'Education'
        verbose_name_plural = 'Educations'

    def __str__(self):
        return self.name


class EducationFaculty(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'Faculty'
        verbose_name_plural = 'Faculties'

    def __str__(self):
        return self.name


class Intership(models.Model):
    full_name = models.CharField(max_length=100)
    data_of_birth = models.DateField()
    region = models.ForeignKey(Region, on_delete=models.CASCADE)
    email = models.EmailField(max_length=100)
    phone = PhoneNumberField()
    position = models.CharField(max_length=100)
    start_date_work = models.DateField()
    type_work = models.CharField(max_length=100, choices=TYPE_WORK)
    start_date_study = models.DateField()
    end_date_study = models.DateField()
    gpa = models.FloatField()
    work_experience = models.TextField()
    skills = models.TextField()
    cv = models.FileField(upload_to='cv')

    class Meta:
        verbose_name = 'Intership'
        verbose_name_plural = 'Interships'

    def __str__(self):
        return self.full_name

class CategoryBook(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name



class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='books')
    pages = models.IntegerField()
    year = models.IntegerField()
    language = models.CharField(max_length=100)
    category = models.ForeignKey(CategoryBook, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Book'
        verbose_name_plural = 'Books'

    def __str__(self):
        return self.title