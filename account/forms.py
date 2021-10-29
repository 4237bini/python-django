from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.forms import TextInput, EmailInput, Select, FileInput
from account.models import UserProfile


class CreateUserForm(UserCreationForm):
    email = forms.EmailField(required = True, label="Email", error_messages={'exits':'This already exist'})
    class Meta:
        model = User
        fields = ['username','email','password1','password2']

    def save(self, commit=True):
        user = super(UserCreateForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user  

    def clean_email(self):
        if User.Objects.filter(email=self.cleaned_data['email']).exists():

            raise forms.ValidationError(self.fields['email'.error_messages['exists']]) 
        return self.cleaned_data['email']    
            
        

    # for the placeholder ..............................................
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'placeholder':'Username'})
        self.fields['email'].widget.attrs.update({'placeholder':'Email'})
        self.fields['password1'].widget.attrs.update({'placeholder':'Password'})
        self.fields['password2'].widget.attrs.update({'placeholder':'Repeat password'})


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('firstname', 'lastname', 'email', 'phone', 'address', 'experience', 'profession', 'total', 'description', 'profileimage')