from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
    email = forms.CharField(max_length=254, required=True, widget=forms.EmailInput(),
                            help_text='Required. Inform a valid email address')
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')