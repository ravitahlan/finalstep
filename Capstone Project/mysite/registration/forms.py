from django import forms
from registration.models import UserModel
from django.contrib.auth.models import User
from django.core.validators import validate_email

class UserForm(forms.ModelForm):
    password = forms.CharField(widget = forms.PasswordInput( attrs = { 'class' : 'form-control', 'id':'password-field' }))
    confirm_password = forms.CharField(widget = forms.PasswordInput( attrs = {'class' : 'form-control', 'id':'confirm_password-field' }))

    class Meta():
        model = User
        fields = ['username','email','password', 'confirm_password' ]
        widgets = {
            'username' : forms.TextInput(attrs = {'class' : 'form-control'}),
            'email' : forms.EmailInput(attrs = {'class':'form-control'}),
        }
        #validating the username
    def clean_username(self):
        print("validating username")
        user = self.cleaned_data['username']
        try:
            match = User.objects.get(username = user)
        except:
            return self.cleaned_data['username']
        raise forms.ValidationError('Username already exist')

    def clean_email(self):
        email = self.cleaned_data['email']
        try:
            mt = validate_email(email)
        except:
            return forms.ValidationError("Email is not in the correct format")
    #Validating Password
    def clean_confirm_password(self):
        pas = self.cleaned_data['password']
        repas = self.cleaned_data['confirm_password']

        MIN_LENGTH = 8

        if( pas and repas):
            if(pas != repas):
                raise forms.ValidationError("password and confirm password not matched")
            else:
                if(len(pas) < MIN_LENGTH):
                    raise forms.ValidationError("Password should have atlest 8 characters")
                if( pas.isdigit()):
                    raise forms.ValidationError("Password should contain atleast one alphabet")
