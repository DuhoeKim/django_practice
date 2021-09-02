from typing import ContextManager
from articles.models import Article
from django.shortcuts import redirect, render, get_object_or_404

# Create your views here.
def index(request):
    articles = Article.objects.order_by('-pk')
    context={
        'articles' : articles,
    }
    return render(request, 'articles/index.html', context)

# def new(request):
#     return render(request, 'articles/new.html')

def create(request):
    if request.method == "POST":
        title = request.POST.get('title')
        content = request.POST.get('content')

        article = Article(title=title, content=content)
        article.save()

        return redirect('articles:detail', article.pk)
    else:
        return render(request, 'articles/new.html')

def detail(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)

    context = {
        'article':article
    }
    return render(request, 'articles/detail.html', context)

def edit(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)

    context = {
        'article' : article
    }
    return render(request, 'articles/edit.html', context)

def update(request, article_pk):
    title = request.POST.get('title')
    content = request.POST.get('content')

    article = Article.objects.get(pk=article_pk)
    article.title = title
    article.content = content
    article.save()

    return redirect('articles:detail', article_pk)

def delete(request, article_pk):
    if request.method == 'POST':
        article = Article.objects.get(pk=article_pk)
        article.delete()

        return redirect('articles:index')
