from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from django.utils.translation import ugettext_lazy as _

User = get_user_model()


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)
    email = forms.EmailField(max_length=254)

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'password1', 'password2', )


class CustomUserChangeForm(forms.ModelForm):

    verify_password = forms.CharField(max_length=255)

    def __init__(self, request, *args, **kwargs):

        self.request = request

        super(CustomUserChangeForm, self).__init__(*args, **kwargs)

    def clean(self):

        cleaned_data = super(CustomUserChangeForm, self).clean()

        password = cleaned_data.get('verify_password')

        if password and self.request.user.check_password(password):
            return cleaned_data

        self.add_error(None, _('Provided password is incorrect'))

    class Meta:
        fields = ('first_name', 'last_name', 'verify_password',
                  'email', 'address', 'phone_number')
        model = User
