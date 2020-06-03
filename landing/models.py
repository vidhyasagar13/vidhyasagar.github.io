# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from datetime import datetime

from django.db import models

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=250)
    description = models.TextField(max_length=2500)
    image = models.ImageField(upload_to='project_images/')
    image_title = models.CharField(max_length=250)
    date = models.DateField()
    created_at = models.DateField(auto_now_add= True)
    updated_at = models.DateField(auto_now_add= True)
    
    def __str__(self):
        return self.title
    
    def __unicode(self):
        return self.title

