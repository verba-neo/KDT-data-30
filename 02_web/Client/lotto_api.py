# Client/lotto_api.py
import requests

for i in range(10000000000):
    res = requests.get('https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo=1086')
data = res.json()
# 로또번호 6개
numbers = [data[f'drwtNo{i}'] for i in range(1, 7)]
# 보너스 번호
bonus_no = data['bnusNo']

print(numbers, bonus_no)

# JSON => 개발자 쓰라고 => Web API
# Application
# Programming
# Interface