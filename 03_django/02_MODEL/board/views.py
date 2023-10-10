# board/views.py
from django.shortcuts import render, redirect

from .models import Article
from .forms import ArticleForm

# Create
def new(request):
    form = ArticleForm()  # input tag 대신 생성
    return render(request, 'board/new.html', {
        'form': form,
    })


def create(request):
    article = Article()
    article.title = request.POST['title']
    article.content = request.POST['content']
    article.save()
    return redirect('board:detail', article.pk)

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
    form = ArticleForm(instance=article)
    
    return render(request, 'board/edit.html', {
        'article': article,
        'form': form,
    })


def update(request, pk):
    article = Article.objects.get(pk=pk)
    article.title = request.POST['title']
    article.content = request.POST['content']
    article.save()
    return redirect('board:detail', article.pk)



# Delete
def delete(request, pk):
    article = Article.objects.get(pk=pk)
    article.delete()
    return redirect('board:index')
