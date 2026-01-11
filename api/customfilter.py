from django_filters import rest_framework as filters
from blogs.models import Blog

class BlogFilter(filters.FilterSet):
    ''' Customized BlogFilter for filtering Posts on basis of Created time'''
    created_at = filters.DateFilter(field_name="created_at", lookup_expr='date')

    class Meta:
        model = Blog
        fields = ['created_at']