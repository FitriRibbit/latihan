#from urllib import request
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def homepage_view(request, *args, **kwargs):
    print(args, kwargs)
    #print(request.user)
    #return HttpResponse ("<h1>Hello World</h1>")
    return render(request, "home.html", {})

def contact_view(request, *args, **kwargs):
    return render(request, "contact.html", {})

def about_view(request, *args, **kwargs):
    my_context = {
        "title" : "this is about us",
        "my_number" : 123,
        "this_is_True": True,
        "my_list" : [123, 435, 335, 345, "About", "Hai"],
        "my_html": "<h1>Hello World</h1>"
    }
    return render(request, "about.html", my_context)

def baseview(request, *args, **kwargs):
    return render(request, "base.html", {})

def navbar_view(request, *args, **kwargs):
    return render(request, "navbar.html", {})

def social_view (request, *args, **kwargs):
    return HttpResponse("<h1>Social Page</h1>")