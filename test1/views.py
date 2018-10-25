#coding=utf-8
from django.http import HttpResponse


def list_view(request):
    return HttpResponse('456')