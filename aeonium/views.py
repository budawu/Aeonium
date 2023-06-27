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
    if article.toc_enable == True:
        article.text = markdown.markdown(article.text,
        extensions=[
            'markdown.extensions.extra',
            'markdown.extensions.codehilite',
            'markdown.extensions.toc',
        ]
        )

    else:
        article.text = markdown.markdown(article.text,
            extensions=[
            'markdown.extensions.extra',
            'markdown.extensions.codehilite',
            ]
        )

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

        'comment': comment,
    }

    return render(request, 'detail.html', context)

def page(request,id):
    '''static page for blog'''
    content = StaticPage.objects.get(id=id)
    if content.toc_enable == True:
        content.content = markdown.markdown(  content.content,
        extensions=[
            'markdown.extensions.extra',
            'markdown.extensions.codehilite',
            'markdown.extensions.toc',
        ]
        )

    else:
            content.content = markdown.markdown(content.content,
            extensions=[
            'markdown.extensions.extra',
            'markdown.extensions.codehilite',
            ]
        )
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
        'comment':comment,
        }
    return render(request,'pages.html',context)
