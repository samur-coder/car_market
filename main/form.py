from django import forms
from .models import Contact_S

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact_S
        fields = ["name", "email", "subject", "message"]
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control p-4", "placeholder": "Your Name"}),
            "email": forms.EmailInput(attrs={"class": "form-control p-4", "placeholder": "Your Email"}),
            "subject": forms.TextInput(attrs={"class": "form-control p-4", "placeholder": "Subject"}),
            "message": forms.Textarea(attrs={"class": "form-control p-3 px-4", "rows": "5", "placeholder": "Message"})
        }
