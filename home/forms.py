from django import forms
from home.models import FeedBack


class FeedBackForm(forms.Form):
    full_name = forms.CharField()
    email = forms.EmailField()
    phone = forms.CharField(label_suffix=' optional:')
    message = forms.CharField(widget=forms.Textarea)

    def save(self):
        feedback = FeedBack(**self.cleaned_data)
        feedback.save()