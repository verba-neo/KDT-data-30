# board/views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_safe, require_POST, require_http_methods

from .models import Article, Comment
from .forms import ArticleForm, CommentForm


@require_http_methods(['GET', 'POST'])
def create(request):
    if request.method == 'GET':
        form = ArticleForm()  # input tag 대신 생성

    elif request.method == 'POST':
        form = ArticleForm(data=request.POST)
        if form.is_valid():
            article = form.save(commit=False)  # 저장하면 작성자 정보 없어서 에러 => 잠깐! 멈춰봐!(commit=False)
            article.user = request.user
            article.save()
            return redirect('board:detail', article.pk)
        
    return render(request, 'board/form.html', {
        'form': form,
    })


# Read
@require_safe
def index(request):
    # 모든 게시글 조회
    articles = Article.objects.all()
    return render(request, 'board/index.html', {
        'articles': articles,
    })


@require_safe
def detail(request, pk):
    article = get_object_or_404(Article, pk=pk)
    # 댓글 작성용 HTML
    form = CommentForm()
    # 댓글 조회용
    # comments = article.comment_set.all()

    return render(request, 'board/detail.html', {
        'article': article,
        'form': form,
    })  


@require_http_methods(['GET', 'POST'])
def update(request, pk):
    article = get_object_or_404(Article, pk=pk)
    
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
@require_POST
def delete(request, pk):
    article = get_object_or_404(Article, pk=pk)
    article.delete()
    return redirect('board:index')
    

@require_POST
def create_comment(request, pk):
    article = get_object_or_404(Article, pk=pk)
    form = CommentForm(data=request.POST)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.article = article
        comment.user = request.user
        comment.save()
    return redirect('board:detail', article.pk)


@require_POST
def delete_comment(request, pk, comment_pk):
    article = get_object_or_404(Article, pk=pk)
    comment = get_object_or_404(Comment, pk=comment_pk)
    comment.delete()
    return redirect('board:detail', article.pk)