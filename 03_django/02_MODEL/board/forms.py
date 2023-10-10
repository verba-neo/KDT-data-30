# board/forms.py
from django import forms
from .models import Article
# 1. 입력 데이터 검증 과정 X
# 2. HTML 만들기 귀찮다

class ArticleForm(forms.ModelForm):
    # 1. 입력 데이터 검증
    # 2. HTML(input/textarea/...)을 생성

    class Meta:
        model = Article
        fields = '__all__'
