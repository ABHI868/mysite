from django import forms
class EmailPostForm(forms.Form):
    name=forms.CharField(max_length=120)
    email=forms.EmailField()
    to=forms.EmailField()
    comments=forms.CharField(max_length=500,required=False, widget=forms.Textarea)