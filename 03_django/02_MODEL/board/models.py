from django.db import models


class Article(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()


# /board/new/ => new 함수 실행 => new.html return (사용자 글을 쓸 곳)
# /board/create/ => create 함수 실행 => 내용 비워놓기
# /board/ => index 함수 실행 => index.html return (글 목록)
# /board/<int:pk>/ => detail 함수 실행(pk 는 변수 라우팅) => detail.html return(글 상세보기)
# /board/edit/ => edit 함수 실행 => edit.html return(글 수정할 곳)
# /board/update/ => update 함수 실행 => 내용 비워두기
# /board/delete/ => delete 함수 실행 => 내용 비워두기