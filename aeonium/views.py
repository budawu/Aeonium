from django.shortcuts import render
from .models import Blog
import markdown

def index(request):
    '''index page'''
    posts  = Blog.objects.order_by('-date')
    context = {'posts':posts}
    return render(request,'aeonium/index.html',context)
    
def detail(request,id):
    '''detail of the article'''
    article = Blog.objects.get(id=id)
    article.text = markdown.markdown(article.text,
        extensions=[
        'markdown.extensions.extra',
        'markdown.extensions.codehilite',
        ])

    context = { 'post': article }
    return render(request, 'aeonium/detail.html', context)