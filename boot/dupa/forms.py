from django import forms

from .models import BillingItem,Paragon



class CeleryForm(forms.ModelForm):
    class Meta:
        model = BillingItem
        fields = ('number_1','number_2')

class ParagonForm(forms.ModelForm):
    class Meta:
        model = Paragon
        fields =('image',)

