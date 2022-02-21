from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse('second_app index page')
