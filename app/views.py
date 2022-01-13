from typing_extensions import Required
from unicodedata import name
from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
from django.http import HttpResponse
from .models import Contact

#https://www.youtube.com/watch?v=Xp85wbIygS4
#https://www.geeksforgeeks.org/python-form-validation-using-django/ validation
#https://www.youtube.com/watch?v=lSgRWA4PMt4&t=590s
def form(request):
    if(request.method=="POST"):
        contact=Contact()
        name=request.POST.get('name')
        email=request.POST.get('email')
        message=request.POST.get('message')
        send_mail(
        'test',
        message,
        settings.EMAIL_HOST_USER,
        [email],
        fail_silently=False,
        )
        contact.name=name
        contact.email=email
        contact.message=message
        contact.save()
        #return HttpResponse("<h1>Thank you Shubham007</h1>")
    return render(request,'form.html')

#def index(request):
#    if request.method=="POST":
#        contact=Contact()
#        email=request.POST.get('email')
#        message=request.POST.get('message')
#        contact.email==email
#        contact.message=message
#        contact.save()
#        return HttpResponse("<h1>Thank you Shubham007</h1>")
#
#    return render(request,'form.html')