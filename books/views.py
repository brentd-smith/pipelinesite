from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("<h1>Hello World of Django, with Heroku and GitHub Pipelines!! Really complicated.</h1>")


def hello(request):
    return HttpResponse("<h2>Hello</h1>")