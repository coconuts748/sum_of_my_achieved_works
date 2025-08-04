import requests
import bs4
from bs4 import BeautifulSoup
import os
import tkinter as tk
from tkinter import messagebox
from tkinter import Canvas
import hashlib
import time

class Base:
    def __init__(self):
        self.all = {}
    def a_d_d(self,name,password):
        self.all[name] = password
    def d_e_l(self,name):
        del self.all[name]
    def c_h_e(self):
        self.all = {}

bb_aa_ss_ee = Base()
na = 'user11';pa = 'password11'
na_after = hashlib.sha256(na.encode('utf-8')).hexdigest()
pa_after = hashlib.sha256(pa.encode('utf-8')).hexdigest()
bb_aa_ss_ee.a_d_d(name= na_after,password=pa_after)
print(bb_aa_ss_ee.all)

# event  event event event
oo = range(1,11)
num = list(oo)
path = 'C:/Users/15125/Desktop/'


# n_a_m_e = os.path.basename(pic_name)
# os.makedirs('pictures', exist_ok=True)
# r_o_a_d = os.path.join('pictures', n_a_m_e)
# with open(r_o_a_d, 'wb') as f:
#     iu = requests.get(pic_href)
#     f.write(iu.content)

def sign_success():
    messagebox.showinfo('登录结果','登录成功！欢迎使用!')

def sign_failure():
    messagebox.showinfo('登录结果','登录失败！账号或密码错误')


def sav_e(event):
    for i in num:
        url = f'https://hdqwalls.com/latest-wallpapers/page/{i}'
        response = requests.get(url)
        soup = bs4.BeautifulSoup(response.text, 'html.parser')
        maintain = soup.find('body')
        then = maintain.find_all('img')
        for img in then:
            # print(img)
            img1 = f'{img}'
            soup = bs4.BeautifulSoup(img1, 'html.parser')
            pic_href = soup.find('img')['src']
            # print(pic_href)
            pic_name = soup.find('img')['title']
            r = requests.get(pic_href)
            os.makedirs('图片集图片集111',exist_ok=True)
            name = os.path.basename(pic_href)
            kll = os.path.join('图片集图片集111',name)
            with open(kll,'wb') as f:
                iu = requests.get(pic_href)
                f.write(iu.content)
                print('this one is done........')
        print('this html is done......')
    print('all done.....')

def s_i_g_n():
    def sign_in():
        user1 = str(get_in.get().strip())
        user_1 = hashlib.sha256(user1.encode('utf-8')).hexdigest()
        user2 = str(get_in2.get().strip())
        user_2 = hashlib.sha256(user2.encode('utf-8')).hexdigest()
        try:
            if user1 and user2:
                if bb_aa_ss_ee.all[user_1] == user_2:
                    if messagebox.askyesno('确认界面', '你确认吗'):
                        messagebox.showinfo('登录结果', '登录成功！欢迎使用!')
                        root.destroy()
                        def locate_save():
                            if sav_e:
                                messagebox.showinfo('结果', '文件已保存！现可在桌面查看')
                            else:
                                messagebox.showwarning('结果', '文件保存失败，请重试！')

                        root1 = tk.Tk()
                        root1.title('保存照片')

                        make = tk.Canvas(width=500, height=300, bg='white')
                        make.pack()
                        make.create_oval(70, 15, 190, 135, fill='blue')
                        make.create_oval(130, 15, 250, 135, fill='blue')
                        make.create_oval(190, 15, 310, 135, fill='blue')
                        make.create_oval(250, 15, 370, 135, fill='blue')
                        make.create_oval(310, 15, 430, 135, fill='blue')
                        make.create_polygon(170, 270, 200, 245, 300, 245, 330, 270, 300, 295, 200, 295, 170, 270,
                                            fill='red')
                        make.create_text(250, 75, text='欢迎使用此工具,这将保存到桌面....', font=('华文彩云', 24),fill='yellow')
                        aa = make.create_text(250, 270, text='下一步', font=('华文彩云', 24),fill='yellow')
                        make.tag_bind(aa, '<Button-1>', sav_e)
                        # if make.tag_bind(aa, '<Button-1>', sav_e):
                        #     messagebox.showinfo('结果','图片现已保存！')
                        root1.mainloop()
                        locate_save()

                    else:
                        messagebox.showinfo('登录结果', '登录失败！账号或密码错误')
        except TypeError as e:
            messagebox.showwarning('错误', '你的输入无效，请重试！,错误类型为{}'.format(e))

    root = tk.Tk()
    root.title('登录界面')
    root.geometry('500x400')

    get_in_tip = tk.Label(root, text='账户:')
    get_in_tip.grid(row=0, column=0, sticky='we')

    get_in = tk.Entry(root)
    get_in.grid(row=0, column=1, sticky='nsew', columnspan=6, padx=2, pady=2)

    get_in2_tip = tk.Label(root, text='密码:')
    get_in2_tip.grid(row=1, column=0, sticky='we')

    get_in2 = tk.Entry(root)
    get_in2.grid(row=1, column=1, columnspan=6, padx=2, pady=2)

    button = tk.Button(root, text='下一步', command=sign_in)
    button.grid(row=2, column=0, sticky='nsew', columnspan=6)

    root.mainloop()
s_i_g_n()


