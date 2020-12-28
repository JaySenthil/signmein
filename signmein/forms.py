# accounts/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser, Meetings, Members

class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'orgName')
        exclude = ('orgNameUrl',)

class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'orgName')
        exclude = ('orgNameUrl',)

class MeetingCreationForm(forms.ModelForm):

    class Meta:
        model = Meetings
        exclude = ('organization',)

class MeetingDeletionForm(forms.ModelForm):

    class Meta:
        model = Meetings
        exclude = ('organization',)

class SignInForm(forms.ModelForm):

    class Meta:
        model = Members
        fields = ('name',)
        exclude = ('orgRef','meetRef',)
