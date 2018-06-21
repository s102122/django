# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.shortcuts import render
import urlparse
import os.path

url_list = []

def index(request):
    return HttpResponse("Hello django")