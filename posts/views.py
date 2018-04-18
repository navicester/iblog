# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages 

from .models import Post
from .forms import PostForm

# Create your views here.
def post_create(request):
    # return HttpResponse("<h1>Create</h1>")
    form = PostForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        messages.success(request, "successfully created")
        return HttpResponseRedirect(instance.get_absolute_url())
    else:
        messages.error(request, "not successfully created")

    context = {
        'form':form
    }

    return render(request, 'post_form.html', context)

def post_detail(request, id=None):
    # return HttpResponse("<h1>Detail</h1>")
    instance = get_object_or_404(Post, id=id)
    context = {
        "title" : instance.title,
        "instance" : instance
    }
    return render(request, "post_detail.html",context)   

def post_update(request, id=None):
    # return HttpResponse("<h1>Update</h1>")
    instance = get_object_or_404(Post, id=id)    
    form = PostForm(request.POST or None, instance=instance)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        messages.success(request, "<a href='# '>item</a> saved", extra_tags="html_safe")
        return HttpResponseRedirect(instance.get_absolute_url())

    context = {
        'form':form,
        "title" : instance.title,
        "instance" : instance
    }

    return render(request, 'post_form.html', context)


def post_delete(request):
    return HttpResponse("<h1>Delete</h1>")

def post_list(request):
    # return HttpResponse("<h1>List</h1>")   

    # if request.user.is_authenticated()  :
    #     context = {
    #         "title" : "my user list"
    #     }
    # else:
    #     context = {
    #         "title" : "list"
    #     }

    queryset = Post.objects.all()
    context = {
        'object_list': queryset,
        'title': 'List',
    }

    return render(request, "index.html",context)      