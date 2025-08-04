# 记账软件:
import time
import tkinter
from tkinter import messagebox
from tkinter.messagebox import askyesno
nowadays = time.asctime(time.localtime(time.time()))
account = 123
code = 456
class Origin:
    def __init__(self, wallet):
        self.wallet = wallet
    def __add__(self, other):
        self.wallet += int(other.wallet)
    def __sub__(self, other):
        self.wallet -= int(other.wallet)

def run():

    def region():
        i1 = int(input1.get().strip())
        i2 = int(input2.get().strip())
        try:
            if i1 == account and i2 == code:
                messagebox.showinfo('登录成功！', '欢迎使用')
                get.destroy()

                def addition():
                    def addition2():
                        x = int(xx.get().strip())
                        if askyesno('确认界面', '你确认吗？'):
                            now1 = Origin(x)
                            now1.__add__(x)
                            user_data1 = 'the user wallet:{}'.format(now1.wallet)
                            with open('user_database', 'a') as f:
                                f.write(user_data1)
                            messagebox.showinfo('结果', '你的信息现已储存！')

                    addition1 = tkinter.Tk()
                    addition1.title('收入情况界面')
                    addition1.geometry('300x150')

                    tkinter.Label(addition1, text='增加', fg='grey').pack()
                    xx = tkinter.Entry(addition1)
                    xx.default_text = '在此输入你本次收入额数...'
                    xx.bind('<FocusIn>', click)
                    xx.bind('<FocusOut>', out)
                    xx.insert(0, xx.default_text)
                    xx.pack()
                    next_add = tkinter.Button(addition1, text='完成', command=addition2)
                    next_add.pack()
                    addition1.mainloop()

                def quit1():
                    if messagebox.askyesno('退出确认', '确认退出？'):
                        mode1.destroy()
                        mode1.quit()

                def decrease():
                    def decrease2():
                        c = int(cc.get().strip())
                        if messagebox.askyesno('确认界面', '你确认吗？'):
                            now2 = Origin(c)
                            now2.__sub__(c)
                            user_data2 = 'the user wallet:{}'.format(now2.wallet)
                            with open('user_database', 'a') as f:
                                f.write(user_data2)
                            messagebox.showinfo('结果', '你的信息现已储存！')

                    decrease1 = tkinter.Tk()
                    decrease1.title('支出情况界面')
                    decrease1.geometry('300x150')

                    tkinter.Label(decrease1, text='减少', fg='blue').pack()
                    cc = tkinter.Entry(decrease1)
                    cc.default_text = '在此输入你本次支出额数...'
                    cc.bind('<FocusIn>', click)
                    cc.bind('<FocusOut>', out)
                    cc.insert(0, cc.default_text)
                    cc.pack()
                    de = tkinter.Button(decrease1, text='完成', command=decrease2)
                    de.pack()
                    decrease1.mainloop()

                def origin():
                    def origin2():
                        z = int(zz.get().strip())
                        if askyesno('确认界面', '你确定吗？'):
                            user_data = 'the user wallet:{}'.format(z)
                            now = Origin(z)
                            now.__add__(z)
                            with open('user_database', 'a') as f:
                                f.write(user_data)
                            messagebox.showinfo('结果', '现已确认成功，你当前有{}元'.format(z))

                    origin1 = tkinter.Tk()
                    origin1.title('现有余额界面')
                    origin1.geometry('300x150')

                    tkinter.Label(origin1, text='提示：请先输入当前余额再进行后续操作').pack()

                    tkinter.Label(origin1, text='余额').pack()
                    zz = tkinter.Entry(origin1)
                    zz.default_text = '在此输入你当前余额'
                    zz.bind('<FocusIn>', click)
                    zz.bind('<FocusOut>', out)
                    zz.insert(0, zz.default_text)
                    zz.pack()
                    orig = tkinter.Button(origin1, text='完成', command=origin2)
                    orig.pack()
                    origin1.mainloop()

                mode1 = tkinter.Tk()
                mode1.title('功能大厅')

                ori = tkinter.Button(mode1, text='原始储蓄基础设置', command=origin)
                ori.pack()
                add = tkinter.Button(mode1, text='收入', command=addition)
                add.pack()
                dec = tkinter.Button(mode1, text='支出', command=decrease)
                dec.pack()
                qu = tkinter.Button(mode1, text='退出', command=quit1)
                qu.pack()
                mode1.mainloop()

            else:
                messagebox.showwarning('登录失败！', '账号或密码错误，请重试')
        except ValueError as e:
            messagebox.showwarning('输入错误！', '你输入的{}无效！'.format(e))



    def click(event):
        if event.widget.get() == event.widget.default_text:
            event.widget.delete(0,'end')
            event.widget.config(fg='grey')


    def out(event):
        if event.widget.get() == '':
            event.widget.insert(0, event.widget.default_text)
            event.widget.config(fg='grey')

    get = tkinter.Tk()
    get.title(f'请先登录!  当前时间为:{nowadays}')
    get.geometry('400x300')
    tkinter.Label(get, text='账号').pack()
    input1 = tkinter.Entry(get)
    input1.default_text = '在此输入账号'
    input1.bind('<FocusIn>', click)
    input1.bind('<FocusOut>', out)
    input1.insert(0, input1.default_text)
    input1.pack()

    tkinter.Label(get, text='密码').pack()
    input2 = tkinter.Entry(get)
    input2.default_text = '在此输入密码'
    input2.bind('<FocusIn>', click)
    input2.bind('<FocusOut>', out)
    input2.insert(0, input2.default_text)
    input2.pack()
    reg = tkinter.Button(get,text='下一步', command=region)
    reg.pack()
    get.mainloop()
run()