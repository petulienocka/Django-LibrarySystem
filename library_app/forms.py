from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
import datetime  

from django import forms


class RenewBookForm(forms.Form):
    renewal_date = forms.DateField()

    def clean_renewal_date(self):
        data = self.cleaned_data['renewal_date']

        if data < datetime.date.today():
            raise ValidationError(_('You cant renew in past'))
    
        if data > datetime.date.today() + datetime.timedelta(days=30):
            raise ValidationError(
                _('You cant renew ahead'))

        return data


class RenewCatalogForm(forms.Form):
    renewal_date = forms.DateField()

    def clean_renewal_date(self):
        data = self.cleaned_data['renewal_date']

        if data < datetime.date.today():
            raise ValidationError(_('You cant renew in past'))
    
        if data > datetime.date.today() + datetime.timedelta(days=7):
            raise ValidationError(
                _('You cant renew ahead'))

        return data
