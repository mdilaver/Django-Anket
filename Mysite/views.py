from django.shortcuts import render
from django.views import generic
from django.http import *
from os.path import join
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
TEMPLATE_DIRS = (
    join(BASE_DIR,  'templates'),
)
def merhaba_django(request):
    return HttpResponse(TEMPLATE_DIRS)