from django.shortcuts import render
from datetime import datetime
import requests

def index(request):
    return render(request, 'util/index.html')


def time(request):
    now = datetime.now()
    return render(request, 'util/time.html', {
        'now': now,
    })


def lotto_out(request):

    res = requests.get('https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo=1086')
    data = res.json()

    my = []  # 사용자 input 데이터
    real = []  # 실제 당첨번호 6개
    bonus = ??  # 보너스 번호
