from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, DetailView

from .models import (
    SliderImages,
    PortfolioAboutPage,
    ProjectCompleted,
    Blog,
)


# Create your views here.
def index_view(request):
    return HttpResponse('Hellow world!')


def home(request):
    template = 'blog/index.html'
    # show five slider images at max
    slider_images = SliderImages.objects.all()[:5]
    # show six projects
    projects = ProjectCompleted.objects.all()[:6]
    context = {
        'slider_images': slider_images,
        'projects': projects,
    }
    return render(request, template, context)


class AboutPage(ListView):
    template_name = "blog/about.html"
    model = PortfolioAboutPage
    context_object_name = 'about_object'


class BlogList(ListView):
    template_name = "blog/blog_list.html"
    model = Blog
    paginate_by = 10
    context_object_name = 'blog_list'

class BlogDetailView(DetailView):
    template_name = "blog/blog_detail.html"
    model = Blog
    context_object_name = 'blog_object'
