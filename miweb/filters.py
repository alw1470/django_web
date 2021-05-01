import django_filters
from .models import DatosScrapy

class DatosScrapyFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(lookup_expr='icontains', label ="Titulo")
    denominacion_de_origen = django_filters.CharFilter(lookup_expr='icontains', label ="Denominación de origen")
    class Meta:
        model = DatosScrapy
        fields = ('title', 'denominacion_de_origen')
