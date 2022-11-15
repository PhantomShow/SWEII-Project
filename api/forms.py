from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from .models import Post

class UserCreateForm(UserCreationForm):
    class Meta:
        fields = ('username', 'email', 'password1', 'password2', 'first_name', 'last_name', 
            'user_type','school', 'gpa', 'height_ft', 'height_in','weight_lb', 'profile_pic')
        model = get_user_model()
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args,**kwargs)
        self.fields['username'].label = 'Display Name'
        self.fields['email'].label = 'Email Address'
        self.fields['user_type'].label = 'Scout or Athlete?'
        self.fields['gpa'].label = 'GPA'

class UserEditForm(ModelForm):
    class Meta:
        fields = ('first_name', 'last_name', 'school', 'gpa', 'height_ft', 'height_in', 'weight_lb', 'bio', 'profile_pic')
        model = get_user_model()
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args,**kwargs)
        self.fields['bio'].label = 'Biography'
        self.fields['gpa'].label = 'GPA'

class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ('text',)