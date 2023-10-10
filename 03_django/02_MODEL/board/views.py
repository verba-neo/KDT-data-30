# board/views.py
from django.shortcuts import render, redirect

from .models import Article
from .forms import ArticleForm


def create(request):
    if request.method == 'GET':
        form = ArticleForm()  # input tag 대신 생성

    elif request.method == 'POST':
        form = ArticleForm(data=request.POST)
        if form.is_valid():
            article = form.save()
            return redirect('board:detail', article.pk)
        
    return render(request, 'board/form.html', {
        'form': form,
    })


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


def update(request, pk):
    article = Article.objects.get(pk=pk)

    if request.method == 'GET':
        form = ArticleForm(instance=article)

    elif request.method == 'POST':
        form = ArticleForm(data=request.POST, instance=article)
        if form.is_valid():
            article = form.save()
            return redirect('board:detail', article.pk)

    return render(request, 'board/form.html', {
        'form': form,
    })


# Delete
def delete(request, pk):
    article = Article.objects.get(pk=pk)
    article.delete()
    return redirect('board:index')
