# board/views.py

from django.shortcuts import render


def new(request):
    return render(request, 'board/new.html')


def create(request):
    pass


def index(request):
    return render(request, 'board/index.html')


def detail(request, pk):
    return render(request, 'board/detail.html')


def edit(request):
    return render(request, 'board/edit.html')


def update(request):
    pass


def delete(request):
    pass
