# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import random

from django.http import FileResponse
from django.shortcuts import render, HttpResponseRedirect,HttpResponse

# Create your views here.
from landing.models import Project


def home(request):
    projects = Project.objects.all()
    skills = ['Data Science', 'Artificial Intelligence', 'PyTorch', 'Pandas', 'Matplotlib', 'Numpy', 'Pyspark', 'Python', 'Netica', 'Jess', 'Ruby', 'Django', 'Ruby On Rails', 'Machine Learning', 'Keras', "PIL", 'CV2','Tensorflow']
    random.shuffle(skills)
    recent_posts = projects.order_by('-created_at')
    recent_posts = recent_posts[0:3]
    recent_posts = recent_posts.values('title','id')
    return render(request,'landing/landing.html',{'projects':projects, 'skills': skills[0:7], 'recent_posts': recent_posts})

def project_read_more(request,id):
    project = Project.objects.get(id=id)
    project_count = Project.objects.all().count()
    random_list = [i for i in range(1,project_count+1)]
    other_project = Project.objects.get(id=random.choice(random_list))
    return render(request, 'landing/project_readmore.html',{'project':project, 'other_project':other_project})

def aboutme(request):
    projects = Project.objects.all()
    skills = ['Data Science', 'Artificial Intelligence', 'PyTorch', 'Pandas', 'Matplotlib', 'Numpy', 'Pyspark',
              'Python', 'Netica', 'Jess', 'Ruby', 'Django', 'Ruby On Rails', 'Machine Learning']
    random.shuffle(skills)
    recent_posts = projects.order_by('-created_at')
    recent_posts = recent_posts[0:3]
    recent_posts = recent_posts.values('title', 'id')
    return render(request, 'landing/aboutme.html',
                  {'projects': projects, 'skills': skills[0:7], 'recent_posts': recent_posts})
