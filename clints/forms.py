from django import forms
from django.contrib.auth.models import User
from .models import Submit_document

class Submit_document_form(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={ "class":"form-control","placeholder":"Put Your Title Hare"}))
    description = forms.CharField(widget=forms.Textarea(attrs={ "class":"form-control","rows":"6","placeholder":"write your project description"}))
    rajuk = forms.FileField(required=False,widget=forms.FileInput(attrs={ "class":"custom-file-input"}))
    wasa = forms.FileField(required=False,widget=forms.FileInput(attrs={ "class":"custom-file-input"}))
    bangladeshBank = forms.FileField(required=False,widget=forms.FileInput(attrs={ "class":"custom-file-input"}))
    titas = forms.FileField(required=False,widget=forms.FileInput(attrs={ "class":"custom-file-input"}))
    pdb = forms.FileField(required=False,widget=forms.FileInput(attrs={ "class":"custom-file-input"}))
    class Meta:
        model = Submit_document
        fields = {'title','description','rajuk','wasa','bangladeshBank','titas','pdb'}
