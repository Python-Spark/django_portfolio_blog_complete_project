from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from ckeditor.fields import RichTextField


class SliderImages(models.Model):
    image = models.ImageField(upload_to='images/slider_images/')
    image_text = models.CharField(max_length=50)


class PortfolioAboutPage(models.Model):
    name = models.CharField(max_length=40)
    description = RichTextField()
    address = models.CharField(max_length=30, blank=True, null=True)
    skills = RichTextField()
    past_work_experiences = RichTextField()
    created_date = models.DateTimeField(auto_now=True)
    updated_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class ProjectCompleted(models.Model):
    project_name = models.CharField(max_length=30)
    project_description = RichTextUploadingField()
    project_picture = models.ImageField(upload_to='images/project_images/')
    created_date = models.DateTimeField(auto_now=True)
    updated_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.project_name


class Blog(models.Model):
    name = models.CharField(max_length=35)
    description = RichTextUploadingField()
    created_date = models.DateTimeField(auto_now=True)
    updated_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
