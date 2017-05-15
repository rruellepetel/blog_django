# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from models import Post, Category

class PostAdmin(admin.ModelAdmin):
    model = Post
    list_display = ('id', 'title', 'creation_date', 'category')
    list_filter = ('category',)
    search_fields = ('title', 'body')
    list_editable = ('title','category')
    # 
    # fieldsets = (
    #     (None, {
    #         "fields" : (('title', 'category'))
    #     }),
    #
    # )



admin.site.register(Post, PostAdmin)




admin.site.register(Category)
