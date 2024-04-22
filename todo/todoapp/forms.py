from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from todoapp.models import Todo

class TodoForm(forms.ModelForm):

    class Meta:
        model=Todo
        # fields="_all_"
        exclude=("created_date","user_object")

class RegistrationForm(UserCreationForm):
    password1=forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control"}))
    password2=forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control"}))   
    class Meta:
        model=User
        fields=["username","email","password1","password2"]
        widgets={
            "username":forms.TextInput(attrs={"class":"form-control"}),
            "email":forms.EmailInput(attrs={"class":"form-control"})
        }

class LoginForm(forms.Form):
    username=forms.CharField()
    password=forms.CharField()