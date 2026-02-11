from django import forms
from .models import Contact


class ContactForm(forms.ModelForm):
    name = forms.CharField(
        widget=forms.TextInput(
            attrs={"class": "input w-full", "placeholder": "Contact Name"}
        )
    )

    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={"class": "input w-full", "placeholder": "Email Address"}
        )
    )

    class Meta:
        model = Contact
        fields = ("name", "email")
