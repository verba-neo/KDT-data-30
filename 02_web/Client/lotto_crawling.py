# Client/lotto_crawling.py
import requests
from bs4 import BeautifulSoup

res = requests.get('https://dhlottery.co.kr/common.do?method=main')
soup = BeautifulSoup(res.text, 'html.parser')

numbers = []

for i in range(1, 7):
    num = int(soup.select_one(f'#drwtNo{i}').text)
    numbers.append(num)

bonus_no = int(soup.select_one('#bnusNo').text)

print(numbers, bonus_no)

# HTML => 정보 긁기(scraping) => GUI