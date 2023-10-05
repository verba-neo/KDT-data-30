# board/views.py
from django.shortcuts import render, redirect

from .models import Article

# Create
def new(request):
    return render(request, 'board/new.html')


def create(request):
    article = Article()
    article.title = request.GET['title']
    article.content = request.GET['content']
    article.save()

    return redirect(f'/board/{article.pk}/')

# Read
def index(request):
    # 모든 게시글 조회
    articles = Article.objects.all()
    return render(request, 'board/index.html', {
        'articles': articles,
    })


def detail(request, pk):
    article = Article.objects.get(pk=pk)
    return render(request, 'board/detail.html', {
        'article': article,
    })  

# Update
def edit(request, pk):
    article = Article.objects.get(pk=pk)
    return render(request, 'board/edit.html', {
        'article': article,
    })


def update(request, pk):
    article = Article.objects.get(pk=pk)
    article.title = request.GET['title']
    article.content = request.GET['content']
    article.save()

    return redirect(f'/board/{article.pk}/')


# Delete
def delete(request, pk):
    article = Article.objects.get(pk=pk)
    article.delete()
    return redirect('/board/')
