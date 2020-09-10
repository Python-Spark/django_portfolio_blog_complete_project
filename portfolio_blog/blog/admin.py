from django.contrib import admin
from .models import (
    PortfolioAboutPage,
    ProjectCompleted,
    SliderImages,
    Blog
)

# Register your models here.
admin.site.register(ProjectCompleted)
admin.site.register(PortfolioAboutPage)
admin.site.register(SliderImages)
admin.site.register(Blog)
