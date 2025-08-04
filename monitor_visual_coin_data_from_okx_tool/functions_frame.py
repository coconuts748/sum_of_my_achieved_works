import tkinter as tk
from tkinter import ttk,messagebox
import time

from promote_tool.the_components import click_to_clean_column, point_out_of_window, check_all_the_coin, \
    looking_for_the_ladder, coin_stage_description_totally, coin_relevant_url, coin_relevant_news, \
    coin_value_data_details
from promote_tool.some_necessary_data import coin_full_name


now = time.asctime(time.localtime(time.time()))

def inner_func_1(coin_name):
    def main_description():
        main_description_text = coin_stage_description_totally(coin_relevant_url(coin_name))
        messagebox.showinfo(f'{coin_name}情况',f'{main_description_text}\n{coin_value_data_details}')

    def today_coin_news():
        today_coin_news_text =coin_relevant_news()
        messagebox.showinfo(f'今日新闻(截止至{now})',f'{today_coin_news_text}')

    def advice():
        messagebox.showinfo('11','制作中,尽请期待....')

    def quit_func():
        if messagebox.askyesno('提示','是否退出当前页面?'):
            inner_func_root.destroy()
            inner_func_root.quit()

    inner_func_root = tk.Tk()
    inner_func_root.title('代币工具')

    inner_func_button = ttk.Button(inner_func_root, text='代币情况', command=main_description)
    inner_func_button.pack()

    inner_func_button_1 = ttk.Button(inner_func_root,text='今日新闻', command=today_coin_news)
    inner_func_button_1.pack()

    inner_func_button_2 = ttk.Button(inner_func_root, text='查看该代码建议', command=advice)
    inner_func_button_2.pack()

    inner_func_button_3 = ttk.Button(inner_func_root,text='退出当前页面', command=quit_func)
    inner_func_button_3.pack()
    inner_func_root.mainloop()


def func_frame():
    def inner_func():
        type_coin_name = str(inputting.get().strip())
        if type_coin_name == '11':
            check_all_the_coin()

        elif type_coin_name == '22':
            looking_for_the_ladder()

        try:
            if messagebox.askyesno('提示','你当前检索的代币为{}\n是否继续?'.format(type_coin_name)):
                relevant_coin_name = coin_full_name[type_coin_name]
                inner_func_root.destroy()
                #对应代码信息框架
                inner_func_1(relevant_coin_name)
                # 对应代码信息框架

        except KeyError or TypeError:
            messagebox.showwarning('错误','你的输入错误或无效,请重试')

    inner_func_root = tk.Tk()
    inner_func_root.title('代币选择界面')

    tips = '注意，使用此工具需要连接外网，如需要请输入11以寻求帮助...'
    coin_tips = tk.Label(inner_func_root,text=f'{tips}')
    coin_tips.grid(column=0, row=0)


    coin_label = tk.Label(inner_func_root,text ='代码名称:')
    coin_label.grid(column=1, row=0)

    inputting = tk.Entry(inner_func_root)
    inputting.default_text = '在此输入你需要查看的代币....'
    inputting.bind('<FocusIn>',click_to_clean_column)
    inputting.bind('<FocusOut>',point_out_of_window)
    inputting.grid(column=1, row=1,columnspan=4)

    coin_tips_1 = tk.Label(inner_func_root,text='如需查看当前支持查看的代码种类,请输入22...')
    coin_tips_1.grid(column=1, row=0)

    inner_func_button = ttk.Button(inner_func_root,text='下一步',command=inner_func)
    inner_func_button.grid(column=2, row=2)
    inner_func_root.mainloop()
