import requests
from bs4 import BeautifulSoup
import time
import hashlib
from tkinter import messagebox,ttk
import tkinter as tk
from promote_tool.some_necessary_data import coin_news_net_header, okx_net_headers, coin_full_name




def coin_relevant_url(coin_name):
    # coin_relevant_full_name = coin_full_name[coin_name]
    url = f'https://www.okx.com/zh-hans/price/{coin_name}'
    return url

def coin_stage_description_totally(url_for_stage_checking):

    r = requests.get(url_for_stage_checking)
    if r.status_code == 200:
        # print(r.content)
        soup = BeautifulSoup(r.content, 'html.parser')
        # print(soup)
        coin_stage_source = soup.find('head')
        coin_stage = coin_stage_source.find_all('meta')[3]
        # for coin in coin_stage:
        #     print(coin)  #描述在“3”
        # print(coin_stage)
        the_direct_detail_about_the_coin = coin_stage['content']
        print(the_direct_detail_about_the_coin)
        return the_direct_detail_about_the_coin
    print(r.status_code)

def coin_relevant_news():
    coin_news_list = []
    r = requests.get('https://www.528btc.com/kx/',headers=coin_news_net_header)
    print(r.status_code)
    if r.status_code == 200:
        # print(r.content)
        soup = BeautifulSoup(r.content, 'lxml')
        news_part_source = soup.find('main')
        # print(news_part_source)
        news_part_source_1 = news_part_source.find_all('div')
        # for i in news_part_source_1:
        #     print(i)
        #     print('#'*99)
        news_part_source_2 = news_part_source_1[0]
        # print(news_part_source_2)
        news_part_source_3 = news_part_source_2.find_all('div')
        # for i in news_part_source_3:
        #     print(i)
        #     print('*'*99)
        news_part_source_4 = news_part_source_3[0]
        # print(news_part_source_4)
        news_part_source_5 = news_part_source_4.find('div',class_='flash')
        # print(news_part_source_5)
        news_part_source_6 = news_part_source_5.find('ul')
        # print(news_part_source_6)
        news_part_source_7 = news_part_source_6.find_all('li')
        for i in news_part_source_7:
            print(i.text.strip())
            # print('*' * 99)
            coin_news_list.append(i.text.strip())
        print('the coin news stored successfully!!!!')
        return coin_news_list
    print(r.status_code)

def coin_value_data_details(visual_coin_relevant_price_url):
    url = 'https://www.okx.com/zh-hans/price/bitcoin-btc'
    r = requests.get(url, headers=okx_net_headers)
    if r.status_code == 200:
        soup = BeautifulSoup(r.content, 'lxml')
        coin_value_source = soup.find('body')
        # print(coin_value_source)
        coin_value_source_1 = coin_value_source.find('div',class_='home-container')
        # print(coin_value_source_1)
        coin_value_source_2 = coin_value_source_1.find('div')
        # print(coin_value_source_2)
        coin_value_source_3 = coin_value_source_2.find('div',class_='index_priceDetailPage__QfBVy index_pageContainer__VCzmQ')
        # print(coin_value_source_3)
        coin_value_source_4 = coin_value_source_3.find_all('div')
        # for i in coin_value_source_4:
        #     print(i)
        #     print('&'*99)
        coin_value_source_5 = coin_value_source_4[6]
        # print(coin_value_source_5)
        coin_value_source_6 = coin_value_source_5.find('div',class_='index_leftContainer__O47Z8')
        # print(coin_value_source_6)
        coin_value_source_7 = coin_value_source_6.find_all('div')
        # for i in coin_value_source_7:
        #     print(i)
        #     print('@'*55)
        coin_value_source_8 = coin_value_source_7[0]
        # print(coin_value_source_8)
        coin_value_source_9 = coin_value_source_8.find_all('div')[0]
        # print(coin_value_source_9)
        coin_value_source_10 = coin_value_source_9.find_all('div')[0]
        # print(coin_value_source_10)
        coin_value_source_11 = coin_value_source_10.find_all('div')[0]
        # print(coin_value_source_11)
        coin_value = coin_value_source_11.text
        print(coin_value)


def encrypt(text):
    random_text = 'key_error_111'
    real_text = f'f{random_text}{text}'
    final_text = hashlib.sha256(real_text.encode('utf-8')).hexdigest()
    # print(final_text)
    return final_text


def click_to_clean_column(event):
    if event.widget.get() == event.widget.default_text:
        event.widget.delete(0, 'end')
        event.widget.config(fg='black')

def point_out_of_window(event):
    if event.widget.get() == '':
        event.widget.insert(0, event.widget.default_text)
        event.widget.config(fg='grey')

def some_comfort_tips_for_coin():
    pass


def check_all_the_coin():
    def coin_sorts_page():
        coin_sorts_page_root.quit()

    coin_sorts_page_root = tk.Tk()
    coin_sorts_page_root.title('代币类别可查询页面')


    coin_sorts_page_text = tk.Label(coin_sorts_page_root,text=f'{coin_full_name}')
    coin_sorts_page_text.pack()

    coin_sorts_page_button = tk.Button(coin_sorts_page_root,text='完成查看',command=coin_sorts_page)
    coin_sorts_page_button.pack()
    coin_sorts_page_root.mainloop()

def looking_for_the_ladder():
    def ladder_page():
        if messagebox.askyesno('再次提醒','加v:123456,发送“66”即可获知!'):
            ladder_page_root.quit()

    ladder_page_root = tk.Tk()
    ladder_page_root.title('梯子获取方式')

    ladder_page_label = tk.Label(ladder_page_root,text='联系方式 加v:123456,发送“66”即可获知!')
    ladder_page_label.pack()

    ladder_page_button = tk.Button(ladder_page_root,text='关闭',command=ladder_page)
    ladder_page_button.pack()
    ladder_page_root.mainloop()