from django.urls import path, include
from .views import HomeView, ArticleDetailView, ScraperView

urlpatterns = [
    path('search', HomeView.as_view(), name='home'),
    path('', ArticleDetailView.as_view(), name='demo-ecommerce'),
    path('articulo/<int:pk>', ArticleDetailView.as_view(), name='article-detail'),
    path('<slug:slug>', ScraperView.as_view(), name='scraper'),
    
]