from django import forms
from email_sender.models import SendEmail

class SendEmailForm(forms.ModelForm):
    class Meta:
        model = SendEmail
        fields = "__all__"