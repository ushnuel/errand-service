from drycleaningApp.models import Message
from django import forms

class MessageForm(forms.ModelForm):

    class Meta():
        model = Message
        fields = ('author', 'phone', 'location', 'text',)
        labels = {
            'author': (''),
            'phone': (''),
            'location': (''),
            'text': (''),
        }
        widgets = {
                'author': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Name - please enter your fullname','name':'author'}),
                'phone': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Phone number','name':'phone'}),
                'location': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Location ex: Opposite Oil and Gas Polythecnic','name':'location'}),
                'text': forms.Textarea(attrs={'class':'form-control', 'placeholder':'Message', 'rows':'6', 'cols':'80', 'name':'text'}),
            }
