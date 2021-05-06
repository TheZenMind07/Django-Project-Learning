from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home_view(request,*args, **kwargs):
        # print(request.user)
        # print(args, kwargs)
        # return HttpResponse("<h1> Hello Django web </h1>")
        return render(request, "index.html", {})


def contact_view(request,*args, **kwargs):
        my_context = {
                "key1" : "Item1",
                "key2" : "item2",
                "arr" : [123,4851,21581,"dfg"]
        }
        return render(request, "contact.html", my_context)

def about_view(request,*args, **kwargs):
        return render(request, "about.html", {})