from django.shortcuts import render
from django.views import generic
from django.http import *
from os.path import join
import os

def merhaba_django(request):
    return HttpResponse(u'Hello')