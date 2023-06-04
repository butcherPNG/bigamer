from datetime import date

from django.utils import timezone
from myapp.models import Request, Feedback, User, Comment
from django import forms
import re
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model

class ReqForm(forms.ModelForm):
    class Meta:
        model = Request
        fields = ('name', 'phone', 'date')

class FeedForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ('name', 'mail', 'message', 'date')

class RegisterUserForm(forms.ModelForm):
    name = forms.CharField(label='Имя', required=True)
    phone = forms.CharField(label='Телефон', required=True)
    mail = forms.CharField(label='Email', required=True)
    username = forms.CharField(label='Имя пользователя', required=False)
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput, required=True)

    class Meta:
        model = User
        fields = ('name', 'phone', 'mail', 'username', 'password')

class CustomAuthenticationForm(forms.Form):
    mail = forms.CharField(label='Email')
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput)

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'message', 'date')