from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def homepath(request):
    return HttpResponse('Its Done..')
    