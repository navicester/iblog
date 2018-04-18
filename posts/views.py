# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404, redirect
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


def post_delete(request, id=None):
    # return HttpResponse("<h1>Delete</h1>")
    instance = get_object_or_404(Post, id=id)    
    instance.delete()
    messages.success(request, "item deleted")
    return redirect("posts:list")


from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

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

    queryset_list = Post.objects.all()

    paginator = Paginator(queryset_list, 2)

    page_var = 'page'
    page = request.GET.get(page_var)
    try:
        queryset = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        queryset = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        queryset = paginator.page(paginator.num_pages)

    context = {
        'object_list': queryset,
        'title': 'List',
        'page_var' : page_var,
    }

    return render(request, "post_list.html",context)      