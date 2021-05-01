from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django_filters.views import FilterView
from django.http import HttpResponse
from django.core.paginator import Paginator
from  .models import Post
from  .models import DatosScrapy
from .filters import DatosScrapyFilter
import request


class HomeView(FilterView, ListView):
    model = DatosScrapy
    template_name = 'home.html'
    paginate_by = 16
    filterset_class = DatosScrapyFilter


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] =DatosScrapyFilter(self.request.GET, queryset=self.get_queryset())
        return context


class ArticleDetailView(ListView):
    model = DatosScrapy
    template_name = 'demo-ecommerce.html'

class ScraperView(DetailView):
    model = DatosScrapy
    template_name = 'scraper.html'
    context_object_name = 'datosscrapy'
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    paginate_by = 5
    filterset_class = DatosScrapyFilter
