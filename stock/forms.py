from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import Customer,Artist,Art,Order,ContactUs,User

class ContactUsForm(forms.ModelForm):
	class Meta:
		model = ContactUs
		fields = ("firstname","lastname","phone","email","text")

class CustomerSignUpForm(forms.ModelForm):
	password = forms.CharField(widget=forms.PasswordInput)
	class Meta:
		model = User
		fields=['username','email','password']
		def save(self, commit=True):
			user = super().save(commit=False)
			user.is_customer=True
			if commit:
				user.save()
			return user


class ArtistSignUpForm(forms.ModelForm):
	password = forms.CharField(widget=forms.PasswordInput)
	class Meta:
		model =User
		fields=['username','email','password']
		def save(self,commit=True):
			user=super().save(commit=False)
			user.is_artist=True
			if commit:
				user.save()
			return user

class CustomerForm(forms.ModelForm):
	class Meta:
		model = Customer
		fields =['name','email','phone','address']


class ArtistForm(forms.ModelForm):
	class Meta:
		model = Artist
		fields =['name','email','phone','address']

class ArtForm(forms.ModelForm):
	class Meta:
		model = Art
		fields = ['name','descrip','price','image','category','quantity']

