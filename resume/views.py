from django.shortcuts import render
from .models import PeopleMessages
from django.http import HttpResponseRedirect
from django.urls import reverse


def home(request):
    return render(request, 'resume/home.html')


def message_from_viewer(request):
    if request.method == "POST":
        u_name = request.POST.get('fullname')
        e_mail = request.POST.get('email')
        msg = request.POST.get('message')
        user_response = PeopleMessages(name=u_name, email=e_mail, message=msg)
        user_response.save()
    return HttpResponseRedirect(reverse('home'))

