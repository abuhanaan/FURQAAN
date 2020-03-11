from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm


class UserCreateForm(UserCreationForm):

    class meta():
        fields = ('username', 'email', 'password1', 'password2')
        model = get_user_model

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.fields['username'].label = 'Display Name'
            self.fields['email'].label = 'Email'
            self.fields['password1'].label = 'Password'
            self.fields['password2'].label = 'Re-enter password'
