# import tkinter as tk
# from tkinter import messagebox
# import time
# import hashlib
# import sys
#
# new = time.asctime(time.localtime(time.time()))
# from tkinter.messagebox import askyesno
#
#
# def hash1(event):
#     return hashlib.sha256(event.encode()).hexdigest()
#
#
# def click(event):
#     if event.widget.get() == event.widget.default_text:
#         event.widget.delete(0, 'end')
#         event.widget.config(fg='black')
#
#
# class Database:
#     def __init__(self):
#         self.data = {}
#
#     def __getitem__(self, account):
#         return self.data.get(account, 'nothing')
#
#     def __setitem__(self, account, code):
#         self.data[account] = code
# m = Database()
# m['account'] = 'manager123'
# m['code'] = 'code456'
#
# u = Database()
# u['account'] = 'user123'
# u['code'] = 'code456'
# y ={u}
#
# class Books:
#     def __init__(self):
#         self.books = {}
#
#     def __getitem__(self, name):
#         return self.books.get(name, 'nothing')
#
#     def __setitem__(self, name, author):
#         self.books[name] = author
#
#     def __add__(self, other):
#         self.books.update(other)
#
#     def __repr__(self):
#         return repr(self.books)
#
# books = Books()
# books['MATH'] = 'math teacher'
# books['ENGLISH'] = 'english teacher'
# books['GEOGRAPHY'] = 'geography teacher'
# books['Chemistry'] = 'chemistry teacher'
# x = {books}
# # print(x)
#
# class Borrow:
#     def __init__(self):
#         self.borrow = {}
#     def __getitem__(self, name):
#         return self.borrow.get(name, 'nothing')
#     def __setitem__(self, name, author):
#         self.borrow[name] = author
#     def __add__(self, other):
#         self.borrow.update(other)
#     def __delitem__(self, name):
#         del self.borrow[name]
#     def __repr__(self):
#         return repr(self.borrow)
# borrow = Borrow()
# def result():
#     def first():
#
#         # text.insert(tk.END, '为确保是真人.....')
#         # basic.update()
#         # time.sleep(2)
#         #
#         # text.insert(tk.END, '现请先通过人坤测试!')
#         # basic.update()
#         # time.sleep(1)
#
#         if int(answer.get().strip()) == 2:
#             if messagebox.askyesno('确认界面', '你确认吗？'):
#                 messagebox.showinfo('答案正确！', '欢迎使用！')
#                 basic.destroy()
#
#                 def contract():
#                     def contract1():
#                         if messagebox.askyesno('确认界面', '真的需要？？'):
#                             if messagebox.askyesno('确认界面（1）', '真的需要？？那就再确认一次'):
#                                 if messagebox.askyesno('确认界面（2）', '好吧,如真的需要那就最后再确认一遍'):
#                                     messagebox.showinfo('联系方式', '加v:123或q:321')
#                                     basic3.destroy()
#
#                     basic3 = tk.Tk()
#                     basic3.title('帮助界面')
#                     basic3.geometry('500x300')
#
#                     but = tk.Button(basic3, text='next', command=contract1)
#                     but.pack()
#                     basic3.mainloop()
#
#                 def manager():
#                     def manager1():
#                         q = str(account1.get())
#                         w = code1.get()
#                         after = hash1(w)
#                         if q and w:
#                             m[w] = after
#                             if messagebox.askyesno('确认界面', '你确认吗？'):
#                                 messagebox.showinfo('登陆成功！', '欢迎回来,管理员{}'.format(q))
#                                 basic1.destroy()
#
#                                 def mine0():
#                                     def mine1():
#                                         if messagebox.askyesno('确认界面', '你确认吗？'):
#                                             return messagebox.showinfo('用户信息为：{}'.format(u.data.items()))
#
#                                     m6 = tk.Tk()
#                                     m6.title('用户信息界面')
#                                     m6.geometry('500x300')
#                                     min1 = tk.Button(m6, text='查询', command=mine1)
#                                     min1.pack()
#                                     mine0_text = tk.Text(m6)
#                                     mine0_text.insert(tk.END, chars='用户信息为：{}'.format(u.data.items()))
#                                     mine0_text.pack()
#                                     m6.mainloop()
#
#                                 def mine2():
#                                     def mine3():
#                                         cc = str(ccc.get().strip())
#                                         dd = str(ddd.get().strip())
#                                         if messagebox.askyesno('确认界面', '你确认吗？'):
#                                             u[cc] = dd
#                                             messagebox.showinfo('添加结果', '用户{}现已被成功添加！'.format(cc))
#                                             mi.destroy()
#
#                                     mi = tk.Tk()
#                                     mi.title('添加用户界面')
#                                     mi.geometry('500x300')
#
#                                     tk.Label(mi, text='账户名').pack()
#                                     ccc = tk.Entry(mi)
#                                     ccc.default_text = '在此输入账户....'
#                                     ccc.insert(0, ccc.default_text)
#                                     ccc.bind('<FocusIn>', click)
#                                     ccc.pack()
#
#                                     tk.Label(mi, text='注册密码').pack()
#                                     ddd = tk.Entry(mi)
#                                     ddd.default_text = '在此输入密码....'
#                                     ddd.insert(0, ddd.default_text)
#                                     ddd.bind('<FocusIn>', click)
#                                     ddd.pack()
#
#                                     button678 = tk.Button(mi, text='下一步', command=mine3)
#                                     button678.pack()
#                                     mi.mainloop()
#
#                                 def mine4():
#                                     def mine5():
#                                         ll = str(lll.get().strip())
#                                         if ll in u.data.items():
#                                             if messagebox.askyesno('确认界面', '你确认吗？'):
#                                                 del u.data[ll]
#                                                 messagebox.showinfo('删除结果', '用户{}现已被成功删除！'.format(ll))
#                                                 mmm.destroy()
#                                         else:
#                                             messagebox.showwarning('错误', '你输入的用户{}错误或不存在！'.format(ll))
#
#
#                                     mmm = tk.Tk()
#                                     mmm.title('删除界面')
#                                     mmm.geometry('500x300')
#
#                                     tk.Label(mmm, text='用户名').pack()
#                                     lll = tk.Entry(mmm)
#                                     lll.default_text = '在此输入需删除的用户名...'
#                                     lll.insert(0, lll.default_text)
#                                     lll.bind('<FocusIn>', click)
#                                     lll.pack()
#                                     mmn = tk.Button(mmm, text='下一步', command=mine5)
#                                     mmn.pack()
#                                     mmm.mainloop()
#                                 gh = tk.Tk()
#                                 gh.title('管理员界面')
#                                 gh.geometry('500x300')
#                                 qw = tk.Button(gh,text='查看用户',command= mine0)
#                                 qw.pack()
#                                 qw1 = tk.Button(gh,text='添加用户',command=mine2)
#                                 qw1.pack()
#                                 qw2 = tk.Button(gh,text='删除用户',command=mine4)
#                                 qw2.pack()
#                                 gh.mainloop()
#                         else:
#                             messagebox.showwarning('登陆失败！', '你的账号或密码错误！')
#
#                     basic1 = tk.Tk()
#                     basic1.title('管理员登录界面')
#                     basic1.geometry('500x300')
#
#                     tk.Label(basic1, text='账号').pack()
#                     account1 = tk.Entry(basic1)
#                     account1.default_text = '在此输入账号...'
#                     account1.insert(0, account1.default_text)
#                     account1.bind('<FocusIn>', click)
#                     account1.pack()
#
#                     tk.Label(basic1, text='密码').pack()
#                     code1 = tk.Entry(basic1)
#                     code1.default_text = '在此输入密码...'
#                     code1.insert(0, code1.default_text)
#                     code1.bind('<FocusIn>', click)
#                     code1.pack()
#
#                     button10 = tk.Button(basic1, text='下一步', command=manager1)
#                     button10.pack()
#                     basic1.mainloop()
#
#                 def exist():
#                     if askyesno('确认界面', '确认退出？'):
#                         basic.quit()
#                         sys.exit()
#
#                 def user():
#                     def user1():
#                         e = str(account2.get())
#                         r = str(code2.get())
#                         after1 = hash1(r)
#                         if e and r:
#                             u[e] = after1
#                             if messagebox.askyesno('确认界面', '你确认吗？'):
#                                 messagebox.showinfo('登录成功！', '欢迎使用，用户{}'.format(e))
#                                 basic2.destroy()
#
#                                 def see():
#                                     def see1():
#                                         if messagebox.askyesno('确认界面', '你确认吗？'):
#                                             for f, g in books.books.items():
#                                                 messagebox.showinfo('查询结果',
#                                                                     '现在可以借阅的书籍有{}:{}'.format(f, g))
#                                                 root456.destroy()
#
#                                     root456 = tk.Tk()
#                                     root456.title('可借阅查询')
#                                     root456.geometry('500x300')
#
#                                     button456 = tk.Button(root456, text='查询', command=see1)
#                                     button456.pack()
#                                     root456.mainloop()
#
#                                 def lending():
#                                     def lending1():
#                                         input1 = str(input2.get().strip())
#                                         if input1 in borrow.borrow:
#                                             if messagebox.askyesno('确认界面', '你确认吗？'):
#                                                 borrow[input1] = '现已借阅'
#                                                 messagebox.showinfo('借阅结果',
#                                                                     '借阅成功！你借阅的书籍为{}'.format(input1))
#                                                 ldg.destroy()
#                                         else:
#                                             messagebox.showwarning('借阅失败！',
#                                                                    '你输入的书籍名{}无效或错误！'.format(input1))
#                                             ldg.destroy()
#
#                                     ldg = tk.Tk()
#                                     ldg.title('借阅界面')
#                                     ldg.geometry('500x300')
#
#                                     input2 = tk.Entry(ldg)
#                                     input2.default_text = '在此输入你借阅的书名...'
#                                     input2.insert(0, input2.default_text)
#                                     input2.bind('<FocusIn>', click)
#                                     input2.pack()
#
#                                     button09 = tk.Button(ldg, text='下一步', command=lending1)
#                                     button09.pack()
#                                     ldg.mainloop()
#
#                                 def return1():
#                                     def return2():
#                                         re = str(ret.get().strip())
#                                         if re in borrow:
#                                             if messagebox.askyesno('确认界面', '你确认吗？'):
#                                                 del borrow[re]
#                                                 messagebox.showinfo('归还结果',
#                                                                     '你之前借阅的书籍{}现已成功归还！'.format(re))
#                                                 return111.destroy()
#                                         else:
#                                             messagebox.showwarning('归还结果',
#                                                                    '归还失败！你输入的书籍{}无效或错误！'.format(re))
#                                             return111.destroy()
#
#                                     return111 = tk.Tk()
#                                     return111.title('归还界面')
#                                     return111.geometry('500x300')
#
#                                     ret = tk.Entry(return111)
#                                     ret.default_text = '在此输入书名...'
#                                     ret.insert(0, ret.default_text)
#                                     ret.bind('<FocusIn>', click)
#                                     ret.pack()
#
#                                     button98 = tk.Button(return111, text='下一步', command=return2)
#                                     button98.pack()
#                                     return111.mainloop()
#                                 ar =tk.Tk()
#                                 ar.title('用户界面')
#                                 ar.geometry('500x300')
#
#                                 bu = tk.Button(ar,text='查看可借阅',command=see)
#                                 bu.pack()
#                                 bu1 = tk.Button(ar,text='借阅',command=lending)
#                                 bu1.pack()
#                                 bu2 = tk.Button(ar,text='归还',command=return1)
#                                 bu2.pack()
#                                 ar.mainloop()
#
#                         else:
#                             messagebox.showwarning('登录失败！', '你的账号或密码错误！')
#
#                     basic2 = tk.Tk()
#                     basic2.title('用户登录界面')
#                     basic2.geometry('500x300')
#
#                     tk.Label(basic2, text='账号').pack()
#                     account2 = tk.Entry(basic2)
#                     account2.default_text = '在此输入账号...'
#                     account2.insert(0, account2.default_text)
#                     account2.bind('<FocusIn>', click)
#                     account2.pack()
#
#                     tk.Label(basic2, text='密码').pack()
#                     code2 = tk.Entry(basic2)
#                     code2.default_text = '在此输入密码...'
#                     code2.insert(0, code2.default_text)
#                     code2.bind('<FocusIn>', click)
#                     code2.pack()
#                     button11 = tk.Button(basic2, text='下一步', command=user1)
#                     button11.pack()
#                     basic2.mainloop()
#                 def check():
#                     def check1():
#                         ff = str(bn.get().strip())
#                         if ff in x:
#                             if messagebox.askyesno('确认界面', '确认查询？'):
#                                 messagebox.showinfo('查询成功！', f'你查询的书{ff}存在！相关作者为{ff[x]}')
#                                 ck.destroy()
#                         else:
#                             messagebox.showinfo('查询失败！', '你查询的{}暂未收录！如需可联系后台人员'.format(ff))
#                             ck.destroy()
#
#                     ck = tk.Tk()
#                     ck.title('查询界面')
#                     ck.geometry('500x300')
#
#                     bn = tk.Entry(ck)
#                     bn.default_text = '在此输入书名...'
#                     bn.insert(0, bn.default_text)
#                     bn.bind('<FocusIn>', click)
#                     bn.pack()
#                     button7 = tk.Button(ck,text='下一步', command=check1)
#                     button7.pack()
#                     ck.mainloop()
#
#                 basin = tk.Tk()
#                 basin.title('主页面')
#                 basin.geometry('500x300')
#
#                 button = tk.Button(basin, text='用户', command=user)
#                 button.pack()
#
#                 button1 = tk.Button(basin, text='管理员', command=manager)
#                 button1.pack()
#
#                 button2 = tk.Button(basin, text='帮助', command=contract)
#                 button2.pack()
#
#                 button3 = tk.Button(basin, text='退出', command=exist)
#                 button3.pack()
#
#                 button4 = tk.Button(basin,text='查询', command=check)
#                 button4.pack()
#                 basic.mainloop()
#         else:
#             messagebox.showwarning('回答错误！', '你是人坤吗？？')
#
#     basic = tk.Tk()
#     basic.title('启动界面, 当前时间为{}'.format(new))
#     basic.geometry('500x300')
#
#     # text = tk.Text(basic)
#     # text.pack()
#     tk.Label(basic, text='为确保是真人，现请先通过人坤测试').pack()
#     tk.Label(basic, text='1+1=').pack()
#     answer = tk.Entry(basic)
#     answer.default_text = '在此输入答案....'
#     answer.insert(0, answer.default_text)
#     answer.bind('<FocusIn>', click)
#     answer.pack()
#     button6 = tk.Button(basic, text='下一步', command=first)
#     button6.pack()
#     basic.mainloop()
#
# result()
#
#
