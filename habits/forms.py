from django import forms
from .models import DailyHabit
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class HabitForm(forms.ModelForm):
    class Meta:
        model = DailyHabit
        fields = ['name', 'description', 'date_added','is_daily','is_completed']

class UserRegistrationForm(UserCreationForm):
        email = forms.EmailField()
        class Meta:
            model = User
            fields = ('username' , 'email' , 'password1' , 'password2' )