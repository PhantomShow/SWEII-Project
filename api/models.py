from django.contrib import auth

# Create your models here.
# Need to fix regular user login and add both athlete and scout model
class User(auth.models.User, auth.models.PermissionsMixin):

    def __str__(self):
        return f"@{self.username}"