from tkinter import ttk, Tk
from tkinter import messagebox
import tkinter as tk
import hashlib
import time

from promote_tool.functions_frame import func_frame
from promote_tool.the_components import encrypt, click_to_clean_column, point_out_of_window

class DATA:
    def __init__(self):
        self.new = {}

    def try_to_append(self, key, value):
        if key is None or value is None:
            pass
        elif len(key) == 0 or len(value) == 0:
            pass
        else:
            real_key = encrypt(key)
            real_value = encrypt(value)
            self.new[real_key] = real_value
        return self.new

    def try_to_delete(self, name):
        if name is  not None:
            pass
        elif len(name) == 0:
            pass
        del self.new[name]
        return self.new

data_manager = DATA()
data_manager.try_to_append('user','code')
print(data_manager.new)

def registration_progress(registration_time):
        def inner_registration_progress_1():
            progress_bar_['value'] = 0
            max_value = 100
            progress_bar_['maximum'] = max_value
            for i in range(max_value + 1):
                progress_bar_['value'] = i
                progress_root.update_idletasks()
                time.sleep(registration_time)
            if messagebox.askyesno('congratulations!','已完成注册!\n是否退出当前程序?\n请点击是以退出....'):
                progress_root.destroy()
                progress_root.quit()

        progress_root = tk.Tk()
        progress_root.title('注册中...')

        progress_bar_ = ttk.Progressbar(progress_root, orient='horizontal', length=200, mode='determinate')
        progress_bar_.pack()

        progress_button = tk.Button(progress_root, text='确认注册', command=inner_registration_progress_1)
        progress_button.pack()
        progress_root.mainloop()

def go_to_login():
    def inner_go_to_login():
        inner_go_to_login_name = str(inner_go_to_login_name_1.get().strip())
        inner_go_to_login_code = str(inner_go_to_login_code_1.get().strip())
        real_inner_go_to_login_name = encrypt(inner_go_to_login_name)
        real_inner_go_to_login_code = encrypt(inner_go_to_login_code)
        try:
            if data_manager.new[real_inner_go_to_login_name] == real_inner_go_to_login_code:
                if messagebox.askyesno('congratulation!','登陆成功,欢迎:\n{}\n是否进行下一步？'.format(inner_go_to_login_name)):
                    inner_go_to_login_root.destroy()
                    func_frame()  #功能框架


        except TypeError or  KeyError:
            messagebox.showwarning('错误','你的输入存在错误,请检查后重试!')

    inner_go_to_login_root = tk.Tk()
    inner_go_to_login_root.title('登陆界面')

    inner_go_to_login_name_1_label = tk.Label(inner_go_to_login_root,text='账号:')
    inner_go_to_login_name_1_label.grid(row=0, column=0)

    inner_go_to_login_name_1 = tk.Entry(inner_go_to_login_root)
    inner_go_to_login_name_1.default_text = '在此输入你的账号...'
    inner_go_to_login_name_1.insert(0,inner_go_to_login_name_1.default_text)
    inner_go_to_login_name_1.bind('<FocusIn>', click_to_clean_column)
    inner_go_to_login_name_1.bind('<FocusOut>', point_out_of_window)
    inner_go_to_login_name_1.grid(row=0, column=1,columnspan=4)

    inner_go_to_login_code_1_label = tk.Label(inner_go_to_login_root,text='密码:')
    inner_go_to_login_code_1_label.grid(row=1, column=0)

    inner_go_to_login_code_1 = tk.Entry(inner_go_to_login_root,show='*')
    inner_go_to_login_code_1.grid(row=1, column=1,columnspan=4)

    inner_go_to_login_button = tk.Button(inner_go_to_login_root,text='登录',command=inner_go_to_login)
    inner_go_to_login_button.grid(row=2,column=2)



def registration():
    def inner_registration():
        registration_name = str(registration_name_1.get().strip())
        registration_code = str(registration_code_1.get().strip())
        if registration_name is None or registration_code is None:
            messagebox.showwarning('提示','你的输入无效!')
        real_registration_name = encrypt(registration_name)
        real_registration_code = encrypt(registration_code)
        if messagebox.askyesno('提示','是否进行下一步?'):
            try:
                start_time = time.time()
                data_manager.try_to_append(key=real_registration_name, value=real_registration_code)
                finish_time = time.time()
                total_time = finish_time - start_time

                registration_progress(total_time) #进度条.....
                save_message = f'{registration_name}:{registration_code}'
                with open('the_saved_message.txt','a') as f:
                    f.write(save_message)
                messagebox.showinfo('提示',f'你当前注册的信息为:\n账号:{registration_name}\n密码:{registration_code}\n该信息以保存至....')
                go_to_login() #去登陆
                root.destroy()

            except KeyError as e:
                print(e)
                messagebox.showwarning('提示', '当前系统故障,请联系后台人员进行维护!')


    root = Tk()
    root.title('注册界面')

    label_1 = tk.Label(root,text='账号:')
    label_1.grid(row=0, column=0)

    registration_name_1 = tk.Entry(root)
    registration_name_1.default_text = '在此输入你的账号....'
    registration_name_1.insert(0,registration_name_1.default_text)
    registration_name_1.bind('<FocusIn>',click_to_clean_column)
    registration_name_1.bind('<FocusOut>',point_out_of_window)
    registration_name_1.grid(row=0,column = 1,columnspan = 4)

    label_2 = tk.Label(root,text='密码:')
    label_2.grid(row=1, column=0)

    registration_code_1 = tk.Entry(root)
    registration_code_1.default_text = '在此输入你的密码...'
    registration_code_1.insert(0,registration_code_1.default_text)
    registration_code_1.bind('<FocusIn>',click_to_clean_column)
    registration_code_1.bind('<FocusOut>',point_out_of_window)
    registration_code_1.grid(row=1,column = 1,columnspan = 4)

    button = tk.Button(root,text='完成注册',command=inner_registration)
    button.grid(row=2,column=2)

    root.mainloop()

registration()