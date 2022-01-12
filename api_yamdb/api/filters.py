from django_filters import CharFilter, FilterSet, NumberFilter
from reviews.models import Title


class TitlesFilter(FilterSet):
    category = CharFilter(field_name='category__slug', lookup_expr='iexact')
    genre = CharFilter(field_name='genre__slug', lookup_expr='iexact')
    name = CharFilter(field_name='name', lookup_expr='contains')
    year = NumberFilter(field_name='year', lookup_expr='iexact')

    class Meta:
        model = Title
        fields = ('category', 'genre', 'name', 'year')
