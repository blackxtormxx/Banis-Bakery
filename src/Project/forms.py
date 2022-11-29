from django import forms
from .models import Item
from django.db.models import fields
from django.forms import ModelForm
from .models import Customorder

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
# DataFlair


class ItemCreate(forms.ModelForm):
    class Meta:
        model = Item
        fields = '__all__'


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

# special order


class CustomorderForm(ModelForm):
    class Meta:
        model = Customorder
        fields = ['name', 'email', 'address',
                  'phone', 'delivery', 'description']
        # widgets = {
        #     'delivery':forms.RadioSelect()
        # }



# Delivery

class RouteDetalisForm(forms.ModelForm):
    class Meta:
        model = RouteDetails
        fields = '__all__'




# Employee

class addEmployeeform(ModelForm):
    class Meta:
        model = Employee
        fields = {'id', 'ename', 'email', 'address', 'contactnumber', 'gender',
                  'jobtitle', 'basicsalary', 'othours', 'otrate', 'allowances', 'netsalary'}
