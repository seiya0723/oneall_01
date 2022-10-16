from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser


from django import forms

class SignupForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model   = CustomUser
        fields  = ["username", "email", "handle_name"]



class CustomUserEditForm(forms.ModelForm):
    class Meta():
        model   = CustomUser
        fields  = [ "handle_name","icon","introduction", ]



