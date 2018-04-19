
from django import forms
from pagedown.widgets import PagedownWidget
from .models import Post

class PostForm(forms.ModelForm):
    publish = forms.DateField(widget=forms.SelectDateWidget)
    content = forms.CharField(widget=PagedownWidget)
    class Meta:
        model = Post
        fields = [
            'title',
            'image',
            'content',
            'draft',
            'publish'
        ]