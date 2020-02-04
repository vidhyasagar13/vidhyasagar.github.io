# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, HttpResponseRedirect,HttpResponse

# Create your views here.
def home(request):
    # return render(HttpResponseRedirect('Hello'))
    # return HttpResponse('hello')
    return render(request,'landing/landing.html')