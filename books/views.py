from django.shortcuts import render
from django.http import HttpResponse
import os

# Create your views here.
def index(request):
    return HttpResponse("<h1>Hello World of Django, with Heroku and GitHub Pipelines!! Really complicated.</h1>")


def hello(request):
    env = os.environ['APPLICATION_ENVIRONMENT'] 
    return HttpResponse("<h2>Hello {}</h1>".format(env))
