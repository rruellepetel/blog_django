# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from autoslug import AutoSlugField

from ckeditor.fields import RichTextField

# Create your models here.
class Category(models.Model):
    label = models.CharField(max_length=50)


    def __unicode__(self):
        return "Catégorie : %s" % self.label

        class Meta:
            verbose_name = "Catégorie"
            verbose_name_plural = "Catégories"

class Post(models.Model):
    title = models.CharField(verbose_name= "Mon Post", max_length=100)
    slug = AutoSlugField(populate_from='title', always_update=True, unique_with=("title",))
    body = RichTextField(verbose_name="Contenu")
    creation_date = models.DateTimeField(auto_now_add=True)

    category = models.ForeignKey(Category)

    def __unicode__(self):
        return self.title

    class Meta:
        verbose_name = "Article"
