
from django import forms

class LoginForm(forms.Form):
    user_name=forms.CharField(required=True,min_length=5)
    Password1=forms.CharField(required=True)

