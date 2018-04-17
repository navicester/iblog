# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def post_create(request):
    return HttpResponse("<h1>Create</h1>")

def post_detail(request):
    # return HttpResponse("<h1>Detail</h1>")
    context = {
        "title" : "detail"
    }
    return render(request, "index.html",context)   

def post_update(request):
    return HttpResponse("<h1>Update</h1>")

def post_delete(request):
    return HttpResponse("<h1>Delete</h1>")

def post_list(request):
    # return HttpResponse("<h1>List</h1>")   
    if request.user.is_authenticated()  :
        context = {
            "title" : "my user list"
        }
    else:
        context = {
            "title" : "list"
        }

    return render(request, "index.html",context)      