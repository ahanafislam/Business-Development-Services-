from django import forms
from django.contrib.auth.models import User
from .models import Provider_submit

class Provider_submit_form(forms.ModelForm):
    accept = forms.BooleanField(widget=forms.CheckboxInput(),initial=False,required=False)
    document = forms.FileField(required=False,widget=forms.FileInput(attrs={ "class":"custom-file-input"}))
    reject = forms.BooleanField(widget=forms.CheckboxInput(),initial=False,required=False)
    feedback = forms.CharField(widget=forms.TextInput(attrs={ "class":"form-control","placeholder":"Put Your Title Hare"}))
    class Meta:
        model = Provider_submit
        fields = {'accept','document','reject','feedback'}
