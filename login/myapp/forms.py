from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate


class SignupUser(UserCreationForm):
	first_name = forms.CharField(max_length=100,required = True)
	last_name =  forms.CharField(max_length=100,required = True)
	email = forms.EmailField(max_length=250)

	class Meta:
		model = User
		fields = ('username','first_name','last_name','password1','password2',)

class UserLoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

    def clean(self, *args, **kwargs):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')

        if username and password:
            user = authenticate(username=username, password=password)
            if not user:
                raise forms.ValidationError('This user does not exist')
            if not user.check_password(password):
                raise forms.ValidationError('Incorrect password')
            if not user.is_active:
                raise forms.ValidationError('This user is not active')
        return super(UserLoginForm, self).clean(*args, **kwargs)


class PostCreate(forms.ModelForm):
    class Meta:
        model = ArticlePkandSlug
        fields = '__all__'
