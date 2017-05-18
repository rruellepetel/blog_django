# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .models import Post, Category
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# Create your views here.

def homepage(request):
    return render(request, "homepage.html")

def post_list(request):
    category = Category.objects.all()
    cat = request.GET.get("category", None)
    page = request.GET.get('page',1)
    if cat :
        # posts = Post.objects.filter(category=cat)
        try :
            categorie = Category.objects.get(id=cat)
            posts = categorie.post_set.all()
        except :
            posts = []
    else :
        posts = Post.objects.all()
        categorie = None

    paginator = Paginator(posts, 25)
    context = {
        "posts" : paginator.page(page),
        "categories" : category,
        "selected_category" : categorie
    }

    return render(request, "post_list.html", context)

def post_detail(request, slug):
    post = Post.objects.get(slug=slug)

    context = {
        "post" : post
    }

    return render(request,'post_detail.html', context)
