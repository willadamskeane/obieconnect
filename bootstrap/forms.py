from django import forms
from django.forms import ModelForm
from django.core.validators import validate_email
from django.contrib.auth.models import User

from bootstrap.models import ExampleFields
from bootstrap.models import User

class ExampleForm(ModelForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={'class':'xlarge'}),min_length=4)
    email = forms.CharField(
        widget=forms.TextInput(attrs={'class':'xlarge'}),min_length=4)
    password = forms.CharField(label='Password',
        widget=forms.PasswordInput(),min_length=4,max_length=30) 
    password_confirm = forms.CharField(label='Repeat Password',
        widget=forms.PasswordInput(),min_length=4,max_length=30)   
    class Meta:
        model = ExampleFields
        
    def clean(self):
        cleaned_data = self.cleaned_data
        password = cleaned_data.get("password")
        password_confirm = cleaned_data.get("password_confirm")
        if password != password_confirm:
            raise forms.ValidationError("Passwords must match.")
    
        return cleaned_data
    
    def save(self, new_data):
        u = User.objects.create_user(new_data['username'],
                                     new_data['email'],
                                     new_data['password1'])
        u.is_active = False
        u.save()
        return u
        
class AjaxAutoComplete(forms.Form):
    name = forms.CharField(help_text="Enter a course name, e.g Psychology 100",
        label="Course Name",
        widget=forms.TextInput(attrs={'class':'xlarge'}))
        
class PopoverForm(forms.Form):
    popover_input = forms.CharField(label="Form Input Popover",
        widget=forms.TextInput(attrs={'class':'xlarge', 
            'data-content' : 'On focus, this appears - defined in forms.py',
            'data-original-title' : 'My title'}))