from django import forms

class MessagesForm(forms.Form):
    title = forms.CharField(max_length=40)
    sender = forms.CharField(max_length=60)
    reciever = forms.CharField(max_length=60)
    content = forms.CharField(max_length=1000)
    date = forms.DateField()