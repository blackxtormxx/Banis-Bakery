from django.db.models import fields
import django_filters
from django_filters import DateFilter

from .models import *


class CustomorderFilter(django_filters.FilterSet):
    # start_date = DateFilter(field_name="date_created", lookup_expr='gte')   #gte=greater than equal
    # end_date = DateFilter(field_name="date_created", lookup_expr='lte')     #lte=less than equal
    class Meta:
        model = Customorder
        fields = ['name', 'status', 'phone']


class employeeFilter(django_filters.FilterSet):
    class Meta:
        model = Employee
        fields = ['id', 'ename']

class ProductFilter(django_filters.FilterSet):
	class Meta:
		model =Product
		fields =['name']
