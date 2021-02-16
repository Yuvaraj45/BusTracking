from django import forms
from .models import user_profile
from django.contrib.auth.models import User

class userregistration(forms.ModelForm):
	password = forms.CharField(widget=forms.PasswordInput())
	confirm_password = forms.CharField(widget=forms.PasswordInput())
	class Meta:
		model = User
		fields = (
			'username',
			'first_name',
			'last_name',
			'email',
		)

class userprofile(forms.ModelForm):
	class Meta:
		model = user_profile
		exclude = ('user',)