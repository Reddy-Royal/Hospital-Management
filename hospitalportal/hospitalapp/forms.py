from django.contrib.auth.forms import UserCreationForm
from django import forms
from . models import User,arogyasri,docprofile,staff
class UserForm(UserCreationForm):
	password1 = forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control my-2","placeholder":"Password"}))
	password2 = forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control my-2","placeholder":"confirm Password "}))
	class Meta:
		model = User
		fields = ["username","uid",]
		widgets ={
		"username":forms.TextInput(attrs={
			"class":"form-control my-2",
			"placeholder":"Username",
			}),
		"uid":forms.TextInput(attrs={
			"class":"form-control my-2",
			"placeholder":"User id",
			}),
		}
class ReForm(forms.ModelForm):
	class Meta:
		model = arogyasri
		fields = ["ufrom","mble","prob"]
		widgets = {
		"ufrom":forms.TextInput(attrs={
			"class":"form-control my-2",
			"placeholder":"Enter Address",
			}),
		"mble":forms.TextInput(attrs={
			"class":"form-control my-2",
			"placeholder":"Enter Mobile Number",
			}),
		"prob":forms.TextInput(attrs={
			"class":"form-control my-2",
			"placeholder":"Your Problem",
			}),


		}
class UsupForm(forms.ModelForm):
	class Meta:
		model = User
		fields =["first_name","last_name","email"]
		widgets = {
		"first_name":forms.TextInput(attrs={
			"class":"form-control my-2",
			"placeholder":"First Name",
			}),
		"last_name":forms.TextInput(attrs={
			"class":"form-control my-2",
			"placeholder":"last Name",
			}),
		"email":forms.TextInput(attrs={
			"class":"form-control my-2",
			"placeholder":"email id",
			}),
		}
class docform(forms.ModelForm):
	class Meta:
		model = docprofile
		fields = ["dname","experience","specialist","mobilenum"]
		widgets = {
		"dname":forms.TextInput(attrs={
			"class":"form-control my-2",
			"placeholder":"doctor name",
			}),
		"experience":forms.TextInput(attrs={
			"class":"form-control my-2",
			"placeholder":"Experience",
			}),
		"specialist":forms.TextInput(attrs={
			"class":"form-control my-2",
			"placeholder":"Specialist",
			}),
		"mobilenum":forms.TextInput(attrs={
			"class":"form-control my-2",
			"placeholder":"Mobile Number",
			}),
		}
class stafform(forms.ModelForm):
	class Meta:
		model = staff
		fields = ["jtitle","jreq","jsal","jexpr","jlocation"]
		widgets = {
		"jtitle":forms.TextInput(attrs={
			"class":"form-control my-2",
			"placeholder":"Specialist",
			}),
		"jsal":forms.TextInput(attrs={
			"class":"form-control my-2",
			"placeholder":"Appointment Fee",
			}),
		"jreq":forms.TextInput(attrs={
			"class":"form-control my-2",
			"placeholder":"Qualification",
			}),
		"jexpr":forms.TextInput(attrs={
			"class":"form-control my-2",
			"placeholder":"Experience",
			}),
		"jlocation":forms.TextInput(attrs={
			"class":"form-control my-2",
			"placeholder":"Location",
			}),
		}

