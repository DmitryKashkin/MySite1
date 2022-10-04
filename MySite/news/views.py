from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    # print(request.META)
    return HttpResponse('<h1>Hello world!</h1')


def test(request):
    # print(request.META)
    return HttpResponse('<h2>Test page</h2')
