from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm
from .models import User, Customer

class UserLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))


class UserRegistrationForm(UserCreationForm):
    role = forms.ChoiceField(choices=User.ROLE_CHOICES)

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2', 'role')

    def save(self, commit=True):
        user = super().save(commit=False)
        if commit:
            user.save()
            Customer.objects.create(user=user)
        return user

class CustomerRegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')

    def save(self, commit=True):
        user = super().save(commit=False)
        user.role = User.CUSTOMER
        if commit:
            user.save()
            Customer.objects.create(user=user)
        return user

class UserPasswordChangeForm(PasswordChangeForm):
    old_password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    new_password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    new_password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
