from django import forms
from api.models import *

class loginForm(forms.Form):
	email = forms.CharField(
		label = 'email',
		widget = forms.EmailInput(attrs={'placeholder': 'Email...', 'class': 'form-control'})
	)

	password = forms.CharField(
		label = 'password',
		widget = forms.PasswordInput(attrs={'placeholder': 'Password...', 'class': 'form-control'})
	)

	remember_me = forms.BooleanField(
		label = 'remember_me'
		widget = forms.CheckboxInput(attrs={'name': 'optionsCheckboxes'})
	)

class signupForm(forms.Form):
	first_name = forms.CharField(
		label = 'first_name',
		widget = forms.TextInput(attrs={'placeholder': 'First Name...', 'class': 'form-control'})
	)

	email = forms.CharField(
		label = 'email',
		widget = forms.EmailInput(attrs={'placeholder': 'Email...', 'class': 'form-control'})
	)

	password = forms.CharField(
		label = 'password',
		widget = forms.PasswordInput(attrs={'placeholder': 'Password...', 'class': 'form-control'})
	)

