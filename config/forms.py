from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model, password_validation
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

    error_messages = {
        'password_mismatch': _("The two password fields didn't match."),
    }

    verify_password = forms.CharField(max_length=255)
    password1 = forms.CharField(max_length=255,
                                required=False,
                                strip=False)
    password2 = forms.CharField(max_length=255,
                                required=False,
                                strip=False,)

    def __init__(self, request, *args, **kwargs):

        self.request = request

        super(CustomUserChangeForm, self).__init__(*args, **kwargs)

    def clean(self):

        cleaned_data = super(CustomUserChangeForm, self).clean()

        password = cleaned_data.get('verify_password')
        if not self.request.user.check_password(password):
            self.add_error(None, _('Current password is incorrect'))
            return

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2:
            if password1 != password2:
                raise forms.ValidationError(
                    self.error_messages['password_mismatch'],
                    code='password_mismatch',
                )
            password_validation.validate_password(password2, self.instance)
        return password2

    def save(self, commit=True):
        password = self.cleaned_data.get("password1")
        if password:
            self.instance.set_password(password)
        return super(CustomUserChangeForm, self).save(commit=commit)

    class Meta:
        fields = ('first_name', 'last_name', 'verify_password',
                  'email', 'address', 'phone_number', 'password1',
                  'password2')
        model = User
