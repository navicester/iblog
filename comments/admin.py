# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import Comment
# Register your models here.

class CommentAdmin(admin.ModelAdmin):
    list_display = ['id', 'content_type', 'object_id', 'content_object', 'parent','is_parent']
    list_display_links = ['id']
    # list_editable = ['title']
    list_filter = ['content_type']
    search_field = ['content']

    class Meta:
        model = Comment 


admin.site.register(Comment, CommentAdmin)
