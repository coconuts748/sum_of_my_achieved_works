import os
import requests
import bs4
from bs4 import BeautifulSoup

# url1 = 'https://pic.5tu.cn/photo/5-1.html'

urls =[]

a = range(1,10)
al_l = list(a)
for x in al_l:
    url2 = f'https://pic.5tu.cn/photo/5-{x}.html'
    urls.append(url2)
    print('this {} is done'.format(url2))
print('done')
# print(urls)
for one in urls:
    url = one
    r = requests.get(url)
    print(r.status_code)
    soup = bs4.BeautifulSoup(r.content, 'html.parser')
    with open('pre.txt', 'w', encoding='utf-8') as f:
        f.write(str(soup))
    body = soup.find('body')
    total = body.find('dd', class_='wall')
    humble = total.find_all('div', class_='img')
    for single_one in humble:
        # print(single_one)
        f = f'{single_one}'
        soup = bs4.BeautifulSoup(f, 'html.parser')
        img_from = soup.find('img')
        # print(img_from)
        s = f'{img_from}'
        soup = bs4.BeautifulSoup(s, 'html.parser')
        # print(soup)
        src = soup.find('img')['src']
        # print(src)
        name = os.path.basename(src)
        os.makedirs('图片集', exist_ok=True)
        save_road = os.path.join('图片集', name)
        with open(save_road, 'wb') as f:
            in1 = requests.get(src)
            f.write(in1.content)
    print('this html is done')
print('all htmls are done')