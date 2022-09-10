from django.shortcuts import render, redirect
from email_sender.models import SendEmail
from email_sender.forms import SendEmailForm
from django.contrib import messages
from django.conf import settings
from django.core.mail import send_mail
# Create your views here.

def send(request):
    if request.method == "POST":
        form = SendEmailForm(request.POST)
        if form.is_valid():
            form.save()
            subject = "message"
            email = form.cleaned_data.get('email')
            message = form.cleaned_data.get('message')
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [email,]
            send_mail( subject, message, email_from, recipient_list )
            return redirect('email_confirm')
        else:
            messages.info(request, "Invalid input")
            return redirect('send')
    form = SendEmailForm()
    context = {'form':form}
    return render(request, 'email_templates.html', context)


def email_confirm(request):
    return render(request, 'email_confirm.html')

