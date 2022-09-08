from django.shortcuts import render, redirect
from email_sender.models import SendEmail
from email_sender.forms import SendEmailForm
from django.contrib import messages
# Create your views here.

def send(request):
    if request.method == "POST":
        form = SendEmailForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('email_confirm')
        else:
            messages.info(request, "Invalid input")
            return redirect('send')
        
    form = SendEmailForm()
    context = {'form':form}
    return render(request, 'email_templates.html', context)


def email_confirm(request):
    return render(request, 'email_confirm.html')

