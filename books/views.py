from django.shortcuts import render
from django.http import HttpResponse
import os

# Create your views here.
def index(request):
    return HttpResponse("<h1>Hello World of Django, with Heroku and GitHub Pipelines!! Really complicated.</h1>")


def hello(request):
    try:
        env = os.environ['APPLICATION_ENVIRONMENT'] or "testing"
    except KeyError:
        env = "review_app"
    return HttpResponse("<h2>Hello {}</h2>".format(env))
