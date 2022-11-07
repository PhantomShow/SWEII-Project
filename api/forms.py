from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm

class UserCreateForm(UserCreationForm):
    class Meta:
        fields = ('username', 'email', 'password1', 'password2', 'first_name', 'last_name', 
            'user_type', 'height_ft', 'height_in', 'profile_pic')
        model = get_user_model()
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args,**kwargs)
        self.fields['username'].label = 'Display Name'
        self.fields['email'].label = 'Email Address'
        self.fields['user_type'].label = 'Scout or Athlete?'

class UserEditForm(ModelForm):
    class Meta:
        fields = ('first_name', 'last_name', 'school', 'height_ft', 'height_in', 'profile_pic')
        model = get_user_model()