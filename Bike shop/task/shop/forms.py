from django import forms

class OrderForm(forms.Form):
    name = forms.CharField(label='your name')
    surname = forms.CharField(label='your surname')
    phone_number = forms.CharField(label='your phone number')
