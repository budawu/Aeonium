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
    context = {
        'posts':posts,
        'title':settings.SITE_NAME,
        'pages':spage
        }

    return render(request,'index.html',context)

def detail(request,id):
    '''detail of the article'''
    article = Blog.objects.get(id=id)
    md = markdown.Markdown(
        extensions=['markdown.extensions.extra',
        'markdown.extensions.codehilite',
        'markdown.extensions.tables',
        'markdown.extensions.toc',
        ])
    article.text = md.convert(article.text)
    comment = f'''
<script src="https://utteranc.es/client.js"
        repo="{settings.COMMENT_REPO}"
        issue-term="pathname"
        theme="github-light"
        crossorigin="anonymous"
        async>
</script>
    '''
    context = {
        'post': article,
        'site_name': settings.SITE_NAME,
        'pages':spage,
        'title':article.title,
        'toc' : md.toc,
        'comment': comment
        }

    return render(request, 'detail.html', context)

def page(request,id):
    '''static page for blog'''
    content = StaticPage.objects.get(id=id)
    md = markdown.Markdown(
        extensions=['markdown.extensions.extra',
        'markdown.extensions.codehilite',
        'markdown.extensions.tables',
        'markdown.extensions.toc',
        ])
    content.content = md.convert(content.content)
    comment = f'''
<script src="https://utteranc.es/client.js"
        repo="{settings.COMMENT_REPO}"
        issue-term="pathname"
        theme="github-light"
        crossorigin="anonymous"
        async>
</script>
    '''
    context = {
        'page':content,
        'site_name':settings.SITE_NAME,
        'pages':spage,
        'title':content.name,
        'toc':md.toc
        }
    return render(request,'pages.html',context)
