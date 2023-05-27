from django import forms
from .models import AddJob,Apply,Info
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm,UsernameField
from django.contrib.auth.models import User

from django.utils.translation import gettext,gettext_lazy as _
class Addjob(forms.ModelForm):
    class Meta:
        model=AddJob
        fields='__all__'
        labels={
            'jobtitle':'Job Title','job_description':'Job Description',
            'requirements':'Job Requirements','add':'job Posted Date','deadline':'Job Dealine'
        }
        widgets={
            'jobtitle':forms.TextInput(attrs={'class':'form-control'}),
            'job_description':forms.Textarea(attrs={'class':'form-control'}),
            'requirements':forms.Textarea(attrs={'class':'form-control'}),
            'add':forms.DateInput(attrs={'class':'form-control'}),
            'deadline':forms.DateInput(attrs={'class':'form-control'}),
        }











class Formaplly(forms.ModelForm):
    class Meta:
        model=Apply
        fields='__all__'
        labels={
            'name':'Candidate Name','email':'Your Email','contact':'Phone','address':'Your Address',
            'education':'Education','obtained_marks':'Obtained Marks','total_marks':'Total Marks',
            'apply':'Application For','resume':'Resume'
        }
        widgets={
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'email':forms.EmailInput(attrs={'class':'form-control'}),
            'contact':forms.NumberInput(attrs={'class':'form-control'}),
            'address':forms.TextInput(attrs={'class':'form-control'}),
            'education':forms.TextInput(attrs={'class':'form-control'}),
            'obtained_marks':forms.TextInput(attrs={'class':'form-control'}),
            'total_marks':forms.TextInput(attrs={'class':'form-control'}),
            'apply':forms.TextInput(attrs={'class':'form-control'}),
            'resume':forms.FileInput(attrs={'class':'form-control'}),
        }












class Companyinfo(forms.ModelForm):
    class Meta:
        model=Info
        fields='__all__'
        labels={
            'name':'Company Name','size':'company Size','location':'comapny Location'
        }
        widgets={
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'size':forms.NumberInput(attrs={'class':'form-control'}),
            'location':forms.TextInput(attrs={'class':'form-control'}),
        }






class Signup(UserCreationForm):
    password1=forms.CharField(label='Password',widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2=forms.CharField(label='Confirm Password',widget=forms.PasswordInput(attrs={'class':'form-control'}))
    class Meta:
        model=User
        fields=['username','first_name','last_name','email']
        labels={
            'username':'User Name','first_name':'First Name','email':'Email'
        }
        widgets={
            'username':forms.TextInput(attrs={'class':'form-control'}),
            'first_name':forms.TextInput(attrs={'class':'form-control'}),
            'last_name':forms.TextInput(attrs={'class':'form-control'}),
            'email':forms.EmailInput(attrs={'class':'form-control'}),
        }




class Loginform(AuthenticationForm):
    username=UsernameField(widget=forms.TextInput(attrs={'auto-focus':True,'class':'form-control'}))
    password=forms.CharField(label=_('Password'),strip=False,
                             widget=forms.PasswordInput(attrs={'autocomplete':'current-password','class':'form-control'}))