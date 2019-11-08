from .models import information
import django_filters

class UserFilter(django_filters.FilterSet):
    class Meta:
        model = information
        fields = ['id', 'name', 'room','floor','date','time','branch','status' ]