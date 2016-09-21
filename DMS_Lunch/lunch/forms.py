from django.forms import EmailField, ModelForm

from django.utils.translation import ugettext_lazy as _

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms

class UserCreationForm(UserCreationForm):
    email = EmailField(label=_("Email address"), required=True,
        help_text=_("Required."))

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

class UserEditForm(ModelForm):
    class Meta:
        model = User
        fields = ["username", "email"]
        