

from django import template
from django.http import HttpResponse, request
from django.template.response import TemplateResponse


def set_castome_cookie(next):
    def middleware_core(request):
        response = next(request)
        response.set_cookie('my_name_is', '42', path='/')
        return response

    return middleware_core


class setCastomeCookie2:
    def __init__(self, next):
        self.next = next

    def __call__(self, request):
        response = self.next(request)
        response.set_cookie('my_lastname_is', '43', path='/')
        return response

    def process_view(self, request, view_func, view_args, view_kwargs):
        pass

    
    def process_template_response(self, request, response):
        return response