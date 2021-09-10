from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User









def Create(UserCreationForm):
    class Meta:
        model=User
        fileds=['first_name','last_name','username','email','password1','password2']
