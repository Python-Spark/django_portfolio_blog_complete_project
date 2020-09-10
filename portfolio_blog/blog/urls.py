from django.urls import path
from .views import index_view, home, AboutPage, BlogList, BlogDetailView

urlpatterns = [
    path('hello/', index_view, name="demo_index_view"),
    path('', home, name="home"),
    path('about/', AboutPage.as_view(), name="about"),
    path('blog/', BlogList.as_view(), name="blog-list"),
    path('blog-detail/<int:pk>/', BlogDetailView.as_view(), name='blog-detail'),
]
