from django import forms
from app.models import UserID
from django.contrib.auth.models import User
from django.contrib.admin import widgets 


class UserRegisterForm(forms.ModelForm):
	password = forms.CharField(widget=forms.PasswordInput())
	confirm_password = forms.CharField(widget=forms.PasswordInput())
	def clean_username(self):
		users = self.cleaned_data["username"]
		if User.objects.filter(username=users).count() > 0:
			raise forms.ValidationError("This username already exists.")
		return users
	def clean(self):
		password = self.cleaned_data.get('password')
		confirm_password = self.cleaned_data.get('confirm_password')
		if password and password != confirm_password:
			raise forms.ValidationError("Passwords don't match.")
		return self.cleaned_data
	class Meta:
		model = User
		fields = ('username','first_name','last_name','password','confirm_password','email')
		
