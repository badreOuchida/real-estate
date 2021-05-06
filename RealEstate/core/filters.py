import django_filters

from .models import Propreties

class PropertieFilter(django_filters.FilterSet):
    location = django_filters.CharFilter(field_name='location', lookup_expr='icontains')
    prop_type = django_filters.CharFilter(field_name='prop_type', lookup_expr='icontains')

    price = django_filters.NumberFilter(field_name='price', lookup_expr='lt')
    class Meta:
        model = Propreties
        fields = ['air','status']