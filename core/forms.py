from django import forms


class OrderForm(forms.Form):
    phone_number = forms.RegexField(regex=r'^\+?1?\d{9,15}$', 
                                error_message = ("Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")) 
    location = forms.CharField()
    comment = forms.CharField()
    item 
    date_create 
    delivery