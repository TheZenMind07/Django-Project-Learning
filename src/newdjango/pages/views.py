from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home_view(request,*args, **kwargs):
        print(request.user)
        print(args, kwargs)
        return HttpResponse("<h1> Hello Django web </h1>")


def contact_view(*args, **kwargs):
        return HttpResponse("<h1>COntact Of the dJangao</h1>")