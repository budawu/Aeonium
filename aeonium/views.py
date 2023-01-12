from django.shortcuts import render
from .models import Blog,StaticPage
import markdown
import sys
sys.path.append('..')
from blog import settings

spage = StaticPage.objects.all()

def index(request):
    '''index page'''
    posts  = Blog.objects.order_by('-date')
    context = {'posts':posts,'site_name':settings.SITE_NAME,'pages':spage}
    return render(request,'aeonium/index.html',context)
    
def detail(request,id):
    '''detail of the article'''
    article = Blog.objects.get(id=id)
    article.text = markdown.markdown(article.text,
        extensions=[
        'markdown.extensions.extra',
        'markdown.extensions.codehilite',
        ])

    context = { 'post': article,'site_name': settings.SITE_NAME,'pages':spage}
    return render(request, 'aeonium/detail.html', context)

def page(request,id):
    '''static page for blog'''
    content = StaticPage.objects.get(id=id)
    content.content = markdown.markdown(content.content,
    extensions=[
        'markdown.extensions.extra',
        'markdown.extensions.codehilite',
        ]
    )
    context = {'page':content,'site_name':settings.SITE_NAME,'pages':spage}
    return render(request,'aeonium/pages.html',context)
