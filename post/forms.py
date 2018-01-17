from django import forms
from .models import Post, Comment
from django.contrib.auth.models import User

class PostForm(forms.ModelForm):
    class Meta: # to link two things together - association
        model = Post
        fields = ['title', 'content', 'photo'] 

class UserSignupForm(forms.ModelForm):
	class Meta:
		model = User
		fields = ['username', 'password']
		widgets = {
            'password': forms.PasswordInput(),
            }

class UserLoginForm(forms.Form):
	username = forms.CharField(required=True)
	password = forms.CharField(required=True, widget=forms.PasswordInput())

class CommentForm(forms.ModelForm):
	class Meta:
		model = Comment
		fields = ['blob']
