from django import forms
from .models import Donation, DonationUserAddress


class DonationForm(forms.ModelForm):

    class Meta:
        model = Donation
        fields = ('payment_method', 'donation_address', 'e20_wallet',
                  'tx_id', 'user')

    def __init__(self, request, *args, **kwargs):
        self.request = request
        super(DonationForm, self).__init__(*args, **kwargs)

    def save(self, commit=True):

        ret = super(DonationForm, self).save(commit=commit)

        if commit:
            # save address
            DonationUserAddress.objects.get_or_create(
                user=self.request.user,
                e20_wallet=ret.e20_wallet
            )

        return ret

    def clean_user(self):
        return self.request.user
