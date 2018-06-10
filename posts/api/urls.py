from django.conf.urls import url
from django.contrib import admin

from .views import (
    PostListAPIView,
    PostDetailAPIView,
    PostUpdateAPIView,
    PostDeleteAPIView,
    )

urlpatterns = [
    url(r'^$', PostListAPIView.as_view(), name="list"),
    url(r'^(?P<slug>[\w-]+)/$', PostDetailAPIView.as_view(), name="detail"),
    url(r'^(?P<slug>[\w-]+)/edit$', PostUpdateAPIView.as_view(), name="update"),
    url(r'^(?P<slug>[\w-]+)/delete$', PostDeleteAPIView.as_view(), name="delete"),
    
    # url(r'^(?P<pk>\d+)/$', PostDetailAPIView.as_view(), name="detail"),
    # url(r'^create/', views.post_create),
    # url(r'^(?P<slug>[\w-]+$)', views.post_detail, name="detail"),    
    # url(r'^(?P<slug>[\w-]+)/edit$', views.post_update, name="update"), 
    # url(r'^(?P<slug>[\w-]+)/delete$', views.post_delete, name="delete"), 
]
