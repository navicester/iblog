# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.contrib import messages 
from django.utils import timezone
from django.db.models  import Q
from urllib import quote_plus

from .models import Post
from .forms import PostForm

from comments.models import Comment

# Create your views here.
def post_create(request):
    # return HttpResponse("<h1>Create</h1>")

    if not request.user.is_staff or not request.user.is_superuser:
        raise Http404

    if not request.user.is_authenticated():
        raise Http404

    form = PostForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.user = request.user
        instance.save()
        messages.success(request, "successfully created")
        return HttpResponseRedirect(instance.get_absolute_url())
    else:
        messages.error(request, "not successfully created")

    context = {
        'form':form
    }

    return render(request, 'post_form.html', context)

def post_detail(request, slug=None):
    # return HttpResponse("<h1>Detail</h1>")
    instance = get_object_or_404(Post, slug=slug)
    if instance.draft or instance.publish > timezone.now().date():
        if not request.user.is_staff or not request.user.is_superuser:
            raise Http404

    share_string = quote_plus(instance.content)
    comments = Comment.objects.filter_by_instance(instance)
    context = {
        "title" : instance.title,
        "instance" : instance,
        "share_string":share_string,
        "comments":comments,

    }
    return render(request, "post_detail.html",context)   

def post_update(request, slug=None):
    # return HttpResponse("<h1>Update</h1>")
    if not request.user.is_staff or not request.user.is_superuser:
        raise Http404

    instance = get_object_or_404(Post, slug=slug)    
    form = PostForm(request.POST or None, request.FILES or None, instance=instance)
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


def post_delete(request, slug=None):
    # return HttpResponse("<h1>Delete</h1>")
    if not request.user.is_staff or not request.user.is_superuser:
        raise Http404

    instance = get_object_or_404(Post, slug=slug)    
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

    queryset_list = Post.objects.active()
    if request.user.is_staff or request.user.is_superuser:
        queryset_list = Post.objects.all()

    query = request.GET.get("q")
    if query:
        queryset_list = queryset_list.filter(
            Q(title__icontains=query) |
            Q(content__icontains=query) | 
            Q(user__first_name__icontains=query) |
            Q(user__last_name__icontains=query)
            ).distinct()

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
        'today': timezone.now().date()
    }

    return render(request, "post_list.html",context)      