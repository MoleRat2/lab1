from django.shortcuts import render
from django.http import HttpResponse
from .services import get_greeting_with_time

def hello_world(request):
    greeting = get_greeting_with_time()
    return HttpResponse(greeting)
