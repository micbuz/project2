from django import forms

from .models import Join


# to nie korzysta w ogole z .models
class EmailForm(forms.Form):
    email = forms.EmailField()


class JoinForm(forms.ModelForm):
    class Meta:
        model = Join
        fields = ('email',)


