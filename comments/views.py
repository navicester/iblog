# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.contrib.contenttypes.models import ContentType


from .models import Comment
from .forms import CommentForm

# Create your views here.
def comment_thread(request, id):
    obj = get_object_or_404(Comment, id=id)
    content_object = obj.content_object
    content_id =content_object.id    

    initial_data = {
        "content_type": obj.content_type, #content_object.get_content_type,
        "object_id":obj.id, #content_id
    }

    form = CommentForm(request.POST or None, initial=initial_data)
    if form.is_valid():
        c_type = form.cleaned_data.get("content_type")
        content_type = ContentType.objects.get(model=c_type)
        obj_id = form.cleaned_data.get('object_id')
        content_data = form.cleaned_data.get('content')
        try:
            parent_id = int(request.POST.get("parent_id")) # not in form
        except:
            parent_id = None

        parent_obj = None
        if parent_id:
            parent_qs = Comment.objects.filter(id=parent_id)
            if parent_qs.exists() and parent_qs.count()==1:
                parent_obj = parent_qs.first()

        new_comment, created = Comment.objects.get_or_create(
            user=request.user,
            content_type=content_type,
            object_id=obj_id,
            content=content_data,
            parent=parent_obj,
            )

        return HttpResponseRedirect(obj.get_absolute_url())

    context = {
        "comment" : obj, 
        "form" : form
    }
    return render(request, "comment_thread.html", context)