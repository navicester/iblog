# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from .models import Post

# Create your views here.
def post_create(request):
    return HttpResponse("<h1>Create</h1>")

def post_detail(request):
    # return HttpResponse("<h1>Detail</h1>")
    instance = get_object_or_404(Post, title="title")
    context = {
        "title" : instance.title,
        "instance" : instance
    }
    return render(request, "post_detail.html",context)   

def post_update(request):
    return HttpResponse("<h1>Update</h1>")

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