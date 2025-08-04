# import tkinter
# from tkinter import messagebox
# from tkinter import font
# from warnings import showwarning
# import pandas as pd
# import os
# import logging
# import hashlib
#
# from click import command
#
#
# def hashing(something):
#     something1 = hashlib.sha256(something.encode('utf-8')).hexdigest()
#     return something1
#
# def click(event):
#     if event.widget.get() == event.widget.default_text:
#         event.widget.delete(0, 'end')
#         event.widget.config(fg='black')
#
# def out(event):
#     if event.widget.get() == '':
#       event.widget.insert(0, event.widget.default_text)
#       event.widget.config(fg='grey')
#
# class DataDeal:
#     def __init__(self):
#         self.dataframe_data = {}
#         self.after_data = {}
#     def add_user(self, user_name,user_password):
#         self.dataframe_data[user_name] = user_password
#         logging.info('已添加账号{}:{}'.format(user_name,user_password))
#         after_user = hashing(user_name);after_password = hashing(user_password)
#         self.after_data[after_user] = after_password
#     def del_user(self, del_user_name):
#         del self.dataframe_data[del_user_name]
#         logging.info('已删除账户号 {}'.format(del_user_name))
#         del self.after_data[hashing(del_user_name)]
#
# data_deal = DataDeal()
# data_deal.add_user('asd','zxc')
# data_deal.add_user('zxc','asd')
#
# print(data_deal.dataframe_data)
# print(data_deal.after_data)
#
#
# column_title_list = []   ;   sets_of_row_single_list=[]  #模式一数据
# the_first_mode_data = {}
#
# def the_first_mode_data_pre(): #仅模式一
#     for y in column_title_list:
#         for t in sets_of_row_single_list:
#             the_first_mode_data[hashing(y)] = t
#
#     return the_first_mode_data
#
#
# single_column_num = []
# def single_column_get(title_number):   #为获取总列数迭代当前进度.......
#     single_column_number = title_number
#     single_column_num.append(single_column_number)
#     return single_column_num
#
# single_row_num = []
# def single_row_get(row_number):   #为获取单列里对确认行数数量迭代的进度.....
#     single_row_number = row_number
#     single_row_num.append(single_row_number)
#     return single_row_num
#
# def the_dealing_row_(someone):
#     def column_content_next_step():
#         one_one_content = []  # 生成一个局部变量,方便进行数据处理.....
#         print('column_content_next_step is running........')
#         print(f'这是该列的第{someone}行')
#
#         single_row_get(someone)  # 获取确认行数迭代里的进度....
#
#         the_single_detail = str(
#             single_detail.get().strip())  # 第六步,确认迭代里各行的具体内容....
#         if the_single_detail is None:
#             messagebox.showwarning('错误', '请输入有效内容！')
#         else:
#             if messagebox.askyesno('提示', f'确认？你的输入内容为{the_single_detail}'):
#                 one_one_content.append(
#                     the_single_detail)  # 对行内容进行处理:1,进行第一次打包(对象为单列)....
#                 sets_of_row_single_list.append(one_one_content)  # 对行内容进行处理:2,进行第二次打包(对象为各列)....
#                 # messagebox.showinfo('提示', f'{single_one}列的数据已成功储存!')
#                 column_content_detail_root.destroy()
#                 return sets_of_row_single_list
#
#     column_content_detail_root = tkinter.Tk()
#     column_content_detail_root.title('单列内容参数获取')
#
#     nowadays_row_number = single_row_num
#     the_true_row_number = len(
#         nowadays_row_number)  # 变相获取行数迭代的进度....
#     true_row_number = int(the_true_row_number) + 2
#
#     tkinter.Label(column_content_detail_root, text=f'现在请输入在第{true_row_number}行(已包括标题)的详细内容!').grid(
#         row=0, column=1, columnspan=2)
#
#     tkinter.Label(column_content_detail_root, text='内容:').grid(row=1, column=0)
#
#     single_detail = tkinter.Entry(column_content_detail_root)
#     single_detail.default_text = '在此输入该列该行的内容....'
#     single_detail.insert(0, single_detail.default_text)
#     single_detail.bind('<FocusIn>', click)
#     single_detail.bind('<FocusOut>', out)
#     single_detail.grid(row=1, column=1, columnspan=3)
#
#     column_content_detail_button = tkinter.Button(column_content_detail_root, text='下一步',
#                                                   command=column_content_next_step)
#     column_content_detail_button.grid(row=2, column=2, rowspan=2)
#     column_content_detail_root.mainloop()
#
# def mode_choose():
#
#     def make_csv_info(detail_data):
#         prepare_dataframe_data = detail_data
#         def make_sure_csv_name():
#             ensure_name = str(input_name.get().strip())
#             if messagebox.askyesno('提示', '确认进入下一步？你设置的名字为{}'.format(ensure_name)):
#                 make_sure_csv_name_root.destroy()
#                 def final_identify():
#                     if messagebox.askyesno('提示', '数据都已备好,是否生成?'):
#                         df = pd.DataFrame(prepare_dataframe_data)
#                         df.to_csv(f'{ensure_name}.csv')
#                         messagebox.showinfo('提示','表格已成功生成!')
#                         final_identify_root.destroy()
#                         final_identify_root.quit()
#
#                 final_identify_root = tkinter.Tk()
#                 final_identify_root.title('最终确认')
#
#                 final_identify_button = tkinter.Button(final_identify_root, text='生成', command=final_identify)
#                 final_identify_button.pack()
#                 final_identify_root.mainloop()
#
#         make_sure_csv_name_root = tkinter.Tk()
#         make_sure_csv_name_root.title('表格名字确认')
#
#         tkinter.Label(make_sure_csv_name_root, text='命名:').grid(row=2, column=0)
#
#         input_name = tkinter.Entry(make_sure_csv_name_root)
#         input_name.default_text = '在此设置表格名字....'
#         input_name.insert(0, input_name.default_text)
#         input_name.bind('<FocusIn>', click)
#         input_name.bind('<FocusOut>', out)
#         input_name.grid(row=2, column=1, columnspan=2)
#
#         make_sure_csv_name_button = tkinter.Button(make_sure_csv_name_root, text='下一步',
#                                                    command=make_sure_csv_name)
#         make_sure_csv_name_button.grid(row=3, column=3)
#         make_sure_csv_name_root.mainloop()
#
#
#
#     def normal_mode():
#         mode_choose_root.destroy()
#         def prepare_for_normal():
#             def inner_prepare_for_normal():
#                 #该菜单界面不可退出......
#                 print('inner_prepare_for_normal is running........')
#                 try:
#                     column_number = int(choose_row_number.get().strip())  # 第一步,先确认总列数....
#                     if column_number <= 0:
#                         messagebox.showwarning('错误', '你的输入无效,请重试！')
#                     else:
#                         if messagebox.askyesno('提示', f'确认？\n你输入的列数为:{column_number}\n是否进入下一步？'):
#                             prepare_normal_root.destroy()
#
#                             def the_next_step():
#                                 print('the_next_step is running........')
#                                 prepare_step_one = range(1, column_number + 1)
#                                 prepare_step_two = list(prepare_step_one)
#                                 for single_one in prepare_step_two:  # 第二步,把总列数迭代,依次进行数据获取....
#                                     single_column_get(single_one)  # 引用函数,以获取当前迭代列数进度....
#                                     print('当前列数进度为{}'.format(single_one))
#                                     the_label_title = str(label_title.get().strip())  # 第三步,获取当前列数的标题....
#                                     if the_label_title is None:
#                                         messagebox.showwarning('错误', '请输入有效值!')
#                                     else:
#                                         if messagebox.askyesno('提示', '确认进入下一步？'):
#                                             column_title_list.append(the_label_title)  # 把各列数的标题以列表格式进行收集.....
#                                             print(f'模式一标题输入为:{column_title_list}')
#                                             next_step_root.destroy()
#
#                                             def the_single_column_content():
#                                                 print('the_single_column_content is running........')
#                                                 the_content_number = int(
#                                                     content_number.get().strip())  # 第四步,在单个列里确认需要输入的行数.....
#                                                 if the_content_number <= 0:
#                                                     messagebox.showwarning('错误', '你的输入为无效值,请重试!')
#                                                 else:
#                                                     if messagebox.askyesno('提示',
#                                                                            '该列行数数量与标题现已成功保存!是否进行下一步?'):
#                                                         column_content_root.destroy()
#
#                                                         need_to_input_number = range(1,
#                                                                                      the_content_number + 1)  # 变相获取前者在单列里确认的行数.....
#                                                         and_the_list = list(need_to_input_number)
#                                                         print('输入的单列里的行数为:', and_the_list)
#                                                         column_content_root.quit()
#                                                         try:
#                                                             for ui in and_the_list:  # 第五步,把前者确认的行数进行迭代依次进行数据获取.....
#                                                                 the_dealing_row_(ui)
#
#                                                         except TypeError as e:
#                                                             print('the error is {}'.format(e))
#
#                                             column_content_root = tkinter.Tk()
#                                             column_content_root.title('单列数据内容数量参数准备')
#
#                                             tkinter.Label(column_content_root,
#                                                           text=f'当前进度为第{the_true_column_number}列')  # 借用之前总列数迭代进度...
#
#                                             tkinter.Label(column_content_root, text='行数:').grid(row=1, column=0)
#
#                                             content_number = tkinter.Entry(column_content_root)
#                                             content_number.default_text = '在此输入你需要的行数.....'
#                                             content_number.insert(0, content_number.default_text)
#                                             content_number.bind('<FocusIn>', click)
#                                             content_number.bind('<FocusOut>', out)
#                                             content_number.grid(row=1, column=1, columnspan=3)
#
#                                             column_content_button = tkinter.Button(column_content_root, text='下一步',
#                                                                                    command=the_single_column_content)
#                                             column_content_button.grid(row=2, column=2)
#                                             column_content_root.mainloop()
#
#                                 if messagebox.showinfo('提示', '所有数据已成功保存!是否进行下一步？'):
#                                     next_step_root.destroy()
#                                     print('模式一的标题集合为{}'.format(column_title_list))
#
#                                     return column_title_list
#
#                             next_step_root = tkinter.Tk()
#                             next_step_root.title('列数参数准备')
#
#                             nowadays_column_number = single_column_num
#                             the_true_column_number = len(nowadays_column_number)  # 变相获取总列数迭代的进度.....
#                             ture_column_number = int(the_true_column_number) + 1
#
#                             tkinter.Label(next_step_root, text='现在输入第{}列的标题'.format(ture_column_number)).grid(
#                                 row=0, column=1, columnspan=3)
#
#                             tkinter.Label(next_step_root, text='标题:').grid(row=1, column=0)
#
#                             label_title = tkinter.Entry(next_step_root)
#                             label_title.default_text = '在此输入此列的标题....'
#                             label_title.insert(0, label_title.default_text)
#                             label_title.bind('<FocusIn>', click)
#                             label_title.bind('<FocusOut>', out)
#                             label_title.grid(row=1, column=1, columnspan=3)
#
#                             next_step_button = tkinter.Button(next_step_root, text='下一步', command=the_next_step)
#                             next_step_button.grid(row=2, column=2, rowspan=2)
#                             next_step_root.mainloop()
#
#                 except TypeError:
#                     messagebox.showwarning('错误', '输入无效,输入内容应为数字!')
#
#             prepare_normal_root = tkinter.Tk()
#             prepare_normal_root.title('选择参数')
#
#             tkinter.Label(prepare_normal_root, text='列数:').grid(row=2, column=0)
#
#             choose_row_number = tkinter.Entry(prepare_normal_root)
#             choose_row_number.default_text = '在此输入你需要的列数....'
#             choose_row_number.insert(0, choose_row_number.default_text)
#             choose_row_number.bind('<FocusIn>', click)
#             choose_row_number.bind('<FocusOut>', out)
#             choose_row_number.grid(row=2, column=1, columnspan=3)
#
#             prepare_normal_button = tkinter.Button(prepare_normal_root, text='完成参数准备',
#                                                    command=inner_prepare_for_normal)
#             prepare_normal_button.grid(row=3, column=2)
#             prepare_normal_root.mainloop()
#
#         def to_make_normal_mode_csv():
#             def inner_to_make_normal_mode_csv():
#                 if messagebox.askyesno('提示', '确认？'):
#                     ##make_up##make_up_##
#                     # the_first_mode_data_pre()
#                     ##make_up##make_up_##
#                     print('模式一的数据内容为{}'.format(the_first_mode_data_pre))
#                     make_csv_info(the_first_mode_data_pre)
#
#             to_make_normal_mode_csv_root = tkinter.Tk()
#             to_make_normal_mode_csv_root.title('表格生成')
#
#             to_make_normal_mode_csv_button = tkinter.Button(to_make_normal_mode_csv_root, text='表格生成',
#                                                             command=inner_to_make_normal_mode_csv)
#             to_make_normal_mode_csv_button.pack()
#             to_make_normal_mode_csv_root.mainloop()
#
#         normal_mode_root = tkinter.Tk()
#         normal_mode_root.title('模式一主界面')
#
#         normal_mode_button = tkinter.Button(normal_mode_root,text='数据保存',command=prepare_for_normal)
#         normal_mode_button.pack()
#
#         normal_mode_button1 = tkinter.Button(normal_mode_root,text='表格生成',command=to_make_normal_mode_csv)
#         normal_mode_button1.pack()
#         normal_mode_root.mainloop()
#
#     def the_pro_mode():
#         mode_choose_root.destroy()
#         column_title_combine1 = []
#         column_row_combine1 = []
#         the_first_mode_data1 = {}
#         column_delete_title_combine = []  # 模式二数据
#
#         the_first_mode_data1_for_show = {}
#         def show_the_image(inner_data):
#             print('show_the_image running....')
#             for q in column_title_combine1:
#                 for w in column_row_combine1:
#                     the_first_mode_data1_for_show[q] = w
#             return the_first_mode_data1_for_show
#
#         def get_origin_data():
#             #不能退出菜单页面...........
#             def prepare_for_pro_mode():
#                 ensure_column = int(column_ensure.get().strip())
#                 ensure_row = int(row_ensure.get().strip())
#                 to_ensure_column = list(range(1, ensure_column + 1))
#                 to_ensure_row = list(range(1, ensure_row + 1))
#                 if messagebox.askyesno('提示', f'确认？\n你输入的列数为{ensure_column}\n你输入的行数为{ensure_row}\n是否进入下一步？'):
#                     prepare_pro_root.destroy()
#
#                     def prepare_ensure_column():
#                         print(to_ensure_column)
#                         for i in to_ensure_column:
#
#                             label_title = '第{}列标题:'.format(i)
#                             tkinter.Label(prepare_ensure_column_root, text=label_title).grid(row=i, column=0)
#
#                             ensure_column_title_content = tkinter.Entry(prepare_ensure_column_root)
#                             ensure_column_title_content.default_text = '在此输入你的标题....'
#                             ensure_column_title_content.insert(0, ensure_column_title_content.default_text)
#                             ensure_column_title_content.bind('<FocusIn>', click)
#                             ensure_column_title_content.bind('<FocusOut>', out)
#                             ensure_column_title_content.grid(row=i, column=1, columnspan=2)
#                             column_title_combine1.append(ensure_column_title_content)
#                             for x in to_ensure_row:
#                                 single_row = []
#                                 label_row = '第{}列“行”内容:'.format(x)
#                                 tkinter.Label(prepare_ensure_column_root, text=label_row).grid(row=i, column=x + 1)
#
#                                 ensure_column_content = tkinter.Entry(prepare_ensure_column_root)
#                                 ensure_column_content.default_text = '在此输入你的内容....'
#                                 ensure_column_content.insert(0, ensure_column_content.default_text)
#                                 ensure_column_content.bind('<FocusIn>', click)
#                                 ensure_column_content.bind('<FocusOut>', out)
#                                 ensure_column_content.grid(row=i, column=x + 2, columnspan=2)
#                                 single_row.append(ensure_column_content)
#                                 column_row_combine1.append(single_row)
#                         prepare_ensure_column_root.destroy()
#                         for r in column_title_combine1:
#                             for e in column_row_combine1:
#                                 the_first_mode_data1[f'{r}'] = e
#                         return column_title_combine1, column_row_combine1,the_first_mode_data1
#
#                     prepare_ensure_column_root = tkinter.Tk()
#                     prepare_ensure_column_root.title('数据整理后续')
#
#                     prepare_ensure_column_button = tkinter.Button(prepare_ensure_column_root, text='下一步',
#                                                                   command=prepare_ensure_column)
#                     prepare_ensure_column_button.grid(row=1, column=2, rowspan=2)
#                     prepare_ensure_column_root.mainloop()
#
#             prepare_pro_root = tkinter.Tk()
#             prepare_pro_root.title('version1.1')
#
#             tkinter.Label(prepare_pro_root, text='先在下面输入你需要的总列数！！后续可修改').grid(row=0, column=2,
#                                                                                                 columnspan=3)
#             tkinter.Label(prepare_pro_root, text='列数:').grid(row=1, column=0)
#
#             column_ensure = tkinter.Entry(prepare_pro_root)
#             column_ensure.default_text = '在此输入你需要的列数....'
#             column_ensure.insert(0, column_ensure.default_text)
#             column_ensure.bind('<FocusIn>', click)
#             column_ensure.bind('<FocusOut>', out)
#             column_ensure.grid(row=1, column=1, columnspan=2)
#
#             tkinter.Label(prepare_pro_root, text='行数:').grid(row=2, column=0)
#
#             row_ensure = tkinter.Entry(prepare_pro_root)
#             row_ensure.default_text = '在此输入你需要的行数....'
#             row_ensure.insert(0, row_ensure.default_text)
#             row_ensure.bind('<FocusIn>', click)
#             row_ensure.bind('<FocusOut>', out)
#             row_ensure.grid(row=2, column=1, columnspan=2)
#             prepare_pro_button = tkinter.Button(prepare_pro_root, text='下一步', command=prepare_for_pro_mode)
#             prepare_pro_button.grid(row=2, column=4)
#             prepare_pro_root.mainloop()
#
#         def to_change_column():
#             def enhance_column():
#                 def inner_enhance_column():##########待处理............................................................................................
#                     print('inner_enhance_column running......')
#                     ensure_enhance_num = int(enhance_num.get().strip())
#                     to_ensure_enhance_num = list(range(1, ensure_enhance_num + 1)) #为下做准备
#                     if messagebox.askyesno('提示', '确认添加数量？'):
#                             def addition_calculation():
#                                 limited_addition = []
#                                 def inner_add_calculation():
#                                     print('inner_add_calculation running......')
#                                     # column_title_combine1 = []; #参考
#                                     # column_row_combine1 = [] #参考
#                                     def step_one():
#                                         print('step_one running......')
#                                         for i in to_ensure_enhance_num:
#                                             tkinter.Label(step_one_root, text='列名:').grid(row=i,column=0)
#
#                                             tt_ext = tkinter.Entry(step_one_root)
#                                             tt_ext.default_text = f'在此设置第{i}列的标题....'
#                                             tt_ext.insert(0, tt_ext.default_text)
#                                             tt_ext.bind('<FocusIn>', click)
#                                             tt_ext.bind('<FocusOut>', out)
#                                             tt_ext.grid(row=i, column=1, columnspan=2)
#
#                                             limited_addition.append(tt_ext)
#                                         return limited_addition
#
#                                     step_one_root = tkinter.Tk()
#                                     step_one_root.title('第一步')
#
#                                     step_one_button = tkinter.Button(step_one_root,text='下一步', command=step_one)
#                                     step_one_button.grid(row=ensure_enhance_num,column=3)
#                                     step_one_root.mainloop()
#
#                                     def step_two():
#                                         print('step_two running......')
#                                         for o in limited_addition:
#                                             to_select_object = str(select_object.get().strip())
#                                             to_select_object1 = str(select_object1.get().strip())
#                                             if len(to_select_object) and len(to_select_object1) is None:
#                                                 messagebox.showwarning('提示', '输入无效或错误!')
#                                             elif to_select_object1 and to_select_object1 in column_title_combine1:
#                                                 if messagebox.askyesno('提示', '是否确认?'):
#                                                     the_selected_object_value = {the_first_mode_data1[to_select_object]}
#                                                     the_selected_object_value1 = {
#                                                         the_first_mode_data1[to_select_object1]}
#                                                     try:
#                                                         use_list = []
#                                                         use_list.append(the_selected_object_value)
#                                                         use_list.append(the_selected_object_value1)
#                                                         the_addition_value = use_list[0] + use_list[1]
#                                                         the_first_mode_data1[o] = the_addition_value
#                                                     except IndexError:
#                                                         messagebox.showwarning('提示','对应键值应为数字！！')
#
#                                             else:
#                                                 messagebox.showwarning('提示', '当前对象不存在')
#
#                                     step_two_root = tkinter.Tk()
#                                     step_two_root.title('选择对象')
#
#                                     tkinter.Label(step_two_root,text='当前表格样式为:').grid(row=1,column=0)
#
#                                     image_show = show_the_image(the_first_mode_data1)
#                                     tkinter.Label(step_two_root,text=f'{image_show}').grid(row=2,column=1)
#
#
#                                     tkinter.Label(step_two_root,text='对象1:').grid(row=3,column=0)
#
#                                     select_object = tkinter.Entry(step_two_root)
#                                     select_object.default_text='在此输入代表对象...'
#                                     select_object.insert(0, select_object.default_text)
#                                     select_object.bind('<FocusIn>', click)
#                                     select_object.bind('<FocusOut>', out)
#                                     select_object.grid(row=3, column=1, columnspan=2)
#
#                                     tkinter.Label(step_two_root,text='对象2:').grid(row=4,column=0)
#
#                                     select_object1 = tkinter.Entry(step_two_root)
#                                     select_object1.default_text = '在此输入代表对象...'
#                                     select_object1.insert(0, select_object1.default_text)
#                                     select_object1.bind('<FocusIn>', click)
#                                     select_object1.bind('<FocusOut>', out)
#                                     select_object1.grid(row=4, column=1, columnspan=2)
#
#                                     additional_details_button = tkinter.Button(step_two_root,text='完成选择',command=step_two)
#                                     additional_details_button.grid(row=5, column=2, columnspan=2)
#                                     step_two_root.mainloop()
#
#
#                                 inner_add_calculation_root = tkinter.Tk()
#                                 inner_add_calculation_root.title('加法详细处理....')
#
#                                 inner_add_calculation_button = tkinter.Button(inner_add_calculation_root,text='下一步',command=inner_add_calculation)
#                                 inner_add_calculation_button.grid(row = ensure_enhance_num+1,column=2)
#
#                                 inner_add_calculation_root.mainloop()
#
#                             def decrease_calculation():
#                                 def inner_decrease_calculation():
#                                     print('inner_decrease_calculation running......')
#                                     limit_decrease = []
#                                     def step_one1():
#                                         print('step_one running......')
#                                         for i in to_ensure_enhance_num:
#                                             tkinter.Label(step_one1_root, text='列名:').grid(row=i,column=0)
#
#                                             tt_ext = tkinter.Entry(step_one1_root)
#                                             tt_ext.default_text = f'在此设置第{i}列的标题....'
#                                             tt_ext.insert(0, tt_ext.default_text)
#                                             tt_ext.bind('<FocusIn>', click)
#                                             tt_ext.bind('<FocusOut>', out)
#                                             tt_ext.grid(row=i, column=1, columnspan=2)
#
#                                             limit_decrease.append(tt_ext)
#                                         return limit_decrease
#
#                                     step_one1_root = tkinter.Tk()
#                                     step_one1_root.title('第一步')
#
#                                     step_one1_button = tkinter.Button(step_one1_root, text='下一步', command=step_one1)
#                                     step_one1_button.grid(row=ensure_enhance_num, column=3)
#                                     step_one1_root.mainloop()
#
#                                     def step_two1():
#                                         print('step_two running......')
#                                         for o in limit_decrease:
#                                             to_select_object = str(select_object.get().strip())
#                                             to_select_object1 = str(select_object1.get().strip())
#                                             if len(to_select_object) and len(to_select_object1) is None:
#                                                 messagebox.showwarning('提示', '输入无效或错误!')
#                                             elif to_select_object1 and to_select_object1 in column_title_combine1:
#                                                 if messagebox.askyesno('提示', '是否确认?'):
#                                                     the_selected_object_value = {the_first_mode_data1[to_select_object]}
#                                                     the_selected_object_value1 = {
#                                                         the_first_mode_data1[to_select_object1]}
#                                                     try:
#                                                         use_list = []
#                                                         use_list.append(the_selected_object_value)
#                                                         use_list.append(the_selected_object_value1)
#                                                         the_addition_value = use_list[0] - use_list[1]
#                                                         the_first_mode_data1[o] = the_addition_value
#                                                         return the_first_mode_data1
#                                                     except IndexError:
#                                                         messagebox.showwarning('提示', '对应键值应为数字！！')
#
#                                             else:
#                                                 messagebox.showwarning('提示', '当前对象不存在')
#
#                                     step_two1_root = tkinter.Tk()
#                                     step_two1_root.title('选择对象')
#
#                                     tkinter.Label(step_two1_root, text='当前表格样式为:').grid(row=1, column=0)
#
#                                     image_show = show_the_image(the_first_mode_data1)
#                                     tkinter.Label(step_two1_root, text=f'{image_show}').grid(row=2, column=1)
#
#                                     tkinter.Label(step_two1_root, text='对象1:').grid(row=3, column=0)
#
#                                     select_object = tkinter.Entry(step_two1_root)
#                                     select_object.default_text = '在此输入代表对象...'
#                                     select_object.insert(0, select_object.default_text)
#                                     select_object.bind('<FocusIn>', click)
#                                     select_object.bind('<FocusOut>', out)
#                                     select_object.grid(row=3, column=1, columnspan=2)
#
#                                     tkinter.Label(step_two1_root, text='对象2:').grid(row=4, column=0)
#
#                                     select_object1 = tkinter.Entry(step_two1_root)
#                                     select_object1.default_text = '在此输入代表对象...'
#                                     select_object1.insert(0, select_object1.default_text)
#                                     select_object1.bind('<FocusIn>', click)
#                                     select_object1.bind('<FocusOut>', out)
#                                     select_object1.grid(row=4, column=1, columnspan=2)
#
#                                     additional_details_button = tkinter.Button(step_two1_root, text='完成选择',
#                                                                                command=step_two1)
#                                     additional_details_button.grid(row=5, column=2, columnspan=2)
#                                     step_two1_root.mainloop()
#
#                                 inner_decrease_calculation_root = tkinter.Tk()
#                                 inner_decrease_calculation_root.title('减法详细处理....')
#
#                                 inner_decrease_calculation_button = tkinter.Button(inner_decrease_calculation_root,text='next',command=inner_decrease_calculation)
#                                 inner_decrease_calculation_button.pack()
#                                 inner_decrease_calculation_root.mainloop()
#
#                             def division_calculation():
#                                 def inner_division_calculation():
#                                     print('inner_division_calculation running......')
#                                     limit_division = []
#
#                                     def step_one2():
#                                         print('step_one running......')
#                                         for i in to_ensure_enhance_num:
#                                             tkinter.Label(step_one2_root, text='列名:').grid(row=i,column=0)
#
#                                             tt_ext = tkinter.Entry(step_one2_root)
#                                             tt_ext.default_text = f'在此设置第{i}列的标题....'
#                                             tt_ext.insert(0, tt_ext.default_text)
#                                             tt_ext.bind('<FocusIn>', click)
#                                             tt_ext.bind('<FocusOut>', out)
#                                             tt_ext.grid(row=i, column=1, columnspan=2)
#
#                                             limit_division.append(tt_ext)
#                                         return limit_division
#
#                                     step_one2_root = tkinter.Tk()
#                                     step_one2_root.title('第一步')
#
#                                     step_one_button = tkinter.Button(step_one2_root, text='下一步', command=step_one2)
#                                     step_one_button.grid(row=ensure_enhance_num, column=3)
#                                     step_one2_root.mainloop()
#
#                                     def step_two2():
#                                         print('step_two running......')
#                                         for o in limit_division:
#                                             to_select_object = str(select_object.get().strip())
#                                             to_select_object1 = str(select_object1.get().strip())
#                                             if len(to_select_object) and len(to_select_object1) is None:
#                                                 messagebox.showwarning('提示', '输入无效或错误!')
#                                             elif to_select_object1 and to_select_object1 in column_title_combine1:
#                                                 if messagebox.askyesno('提示', '是否确认?'):
#                                                     the_selected_object_value = {the_first_mode_data1[to_select_object]}
#                                                     the_selected_object_value1 = {
#                                                         the_first_mode_data1[to_select_object1]}
#                                                     try:
#                                                         use_list = []
#                                                         use_list.append(the_selected_object_value)
#                                                         use_list.append(the_selected_object_value1)
#                                                         the_addition_value = use_list[0] / use_list[1]
#                                                         the_first_mode_data1[o] = the_addition_value
#                                                         return the_first_mode_data1
#                                                     except IndexError:
#                                                         messagebox.showwarning('提示', '对应键值应为数字！！')
#
#                                             else:
#                                                 messagebox.showwarning('提示', '当前对象不存在')
#
#                                     step_two2_root = tkinter.Tk()
#                                     step_two2_root.title('选择对象')
#
#                                     tkinter.Label(step_two2_root, text='当前表格样式为:').grid(row=1, column=0)
#
#                                     image_show = show_the_image(the_first_mode_data1)
#                                     tkinter.Label(step_two2_root, text=f'{image_show}').grid(row=2, column=1)
#
#                                     tkinter.Label(step_two2_root, text='对象1:').grid(row=3, column=0)
#
#                                     select_object = tkinter.Entry(step_two2_root)
#                                     select_object.default_text = '在此输入代表对象...'
#                                     select_object.insert(0, select_object.default_text)
#                                     select_object.bind('<FocusIn>', click)
#                                     select_object.bind('<FocusOut>', out)
#                                     select_object.grid(row=3, column=1, columnspan=2)
#
#                                     tkinter.Label(step_two2_root, text='对象2:').grid(row=4, column=0)
#
#                                     select_object1 = tkinter.Entry(step_two2_root)
#                                     select_object1.default_text = '在此输入代表对象...'
#                                     select_object1.insert(0, select_object1.default_text)
#                                     select_object1.bind('<FocusIn>', click)
#                                     select_object1.bind('<FocusOut>', out)
#                                     select_object1.grid(row=4, column=1, columnspan=2)
#
#                                     additional_details_button = tkinter.Button(step_two2_root, text='完成选择',
#                                                                                command=step_two2)
#                                     additional_details_button.grid(row=5, column=2, columnspan=2)
#                                     step_two2_root.mainloop()
#
#                                 inner_division_calculation_root = tkinter.Tk()
#                                 inner_division_calculation_root.title('除法详细处理....')
#
#                                 inner_division_calculation_button = tkinter.Button(inner_division_calculation_root,
#                                                                                    text='next',
#                                                                                    command=inner_division_calculation)
#                                 inner_division_calculation_button.pack()
#                                 inner_division_calculation_root.mainloop()
#
#                             def multiplication_calculation():
#                                 def inner_multiplication_calculation():
#                                     print('inner_multiplication_calculation running......')
#
#                                     limit_mutiplication = []
#
#                                     def step_one3():
#                                         print('step_one running......')
#                                         for i in to_ensure_enhance_num:
#                                             tkinter.Label(step_one3_root, text='列名:').grid(row=i, column=0)
#
#                                             tt_ext = tkinter.Entry(step_one3_root)
#                                             tt_ext.default_text = f'在此设置第{i}列的标题....'
#                                             tt_ext.insert(0, tt_ext.default_text)
#                                             tt_ext.bind('<FocusIn>', click)
#                                             tt_ext.bind('<FocusOut>', out)
#                                             tt_ext.grid(row=i, column=1, columnspan=2)
#
#                                             limit_mutiplication.append(tt_ext)
#                                         return limit_mutiplication
#
#                                     step_one3_root = tkinter.Tk()
#                                     step_one3_root.title('第一步')
#
#                                     step_one3_button = tkinter.Button(step_one3_root, text='下一步', command=step_one3)
#                                     step_one3_button.grid(row=ensure_enhance_num, column=3)
#                                     step_one3_root.mainloop()
#
#                                     def step_two3():
#                                         print('step_two running......')
#                                         for o in limit_mutiplication:
#                                             to_select_object = str(select_object.get().strip())
#                                             to_select_object1 = str(select_object1.get().strip())
#                                             if len(to_select_object) and len(to_select_object1) is None:
#                                                 messagebox.showwarning('提示', '输入无效或错误!')
#                                             elif to_select_object1 and to_select_object1 in column_title_combine1:
#                                                 if messagebox.askyesno('提示', '是否确认?'):
#                                                     the_selected_object_value = {the_first_mode_data1[to_select_object]}
#                                                     the_selected_object_value1 = {
#                                                         the_first_mode_data1[to_select_object1]}
#                                                     try:
#                                                         use_list = []
#                                                         use_list.append(the_selected_object_value)
#                                                         use_list.append(the_selected_object_value1)
#                                                         the_addition_value = use_list[0] - use_list[1]
#                                                         the_first_mode_data1[o] = the_addition_value
#                                                         return the_first_mode_data1
#                                                     except IndexError:
#                                                         messagebox.showwarning('提示', '对应键值应为数字！！')
#
#                                             else:
#                                                 messagebox.showwarning('提示', '当前对象不存在')
#
#                                     step_two2_root = tkinter.Tk()
#                                     step_two2_root.title('选择对象')
#
#                                     tkinter.Label(step_two2_root, text='当前表格样式为:').grid(row=1, column=0)
#
#                                     image_show = show_the_image(the_first_mode_data1)
#                                     tkinter.Label(step_two2_root, text=f'{image_show}').grid(row=2, column=1)
#
#                                     tkinter.Label(step_two2_root, text='对象1:').grid(row=3, column=0)
#
#                                     select_object = tkinter.Entry(step_two2_root)
#                                     select_object.default_text = '在此输入代表对象...'
#                                     select_object.insert(0, select_object.default_text)
#                                     select_object.bind('<FocusIn>', click)
#                                     select_object.bind('<FocusOut>', out)
#                                     select_object.grid(row=3, column=1, columnspan=2)
#
#                                     tkinter.Label(step_two2_root, text='对象2:').grid(row=4, column=0)
#
#                                     select_object1 = tkinter.Entry(step_two2_root)
#                                     select_object1.default_text = '在此输入代表对象...'
#                                     select_object1.insert(0, select_object1.default_text)
#                                     select_object1.bind('<FocusIn>', click)
#                                     select_object1.bind('<FocusOut>', out)
#                                     select_object1.grid(row=4, column=1, columnspan=2)
#
#                                     additional_details_button = tkinter.Button(step_two2_root, text='完成选择',
#                                                                                command=step_two3)
#                                     additional_details_button.grid(row=5, column=2, columnspan=2)
#                                     step_two2_root.mainloop()
#
#                                 inner_multiplication_calculation_root = tkinter.Tk()
#                                 inner_multiplication_calculation_root.title('乘法详细处理....')
#
#                                 inner_multiplication_calculation_button = tkinter.Button(
#                                     inner_multiplication_calculation_root, text='next',
#                                     command=inner_multiplication_calculation)
#                                 inner_multiplication_calculation_button.pack()
#                                 inner_multiplication_calculation_root.mainloop()
#
#                             prepare_enhance_total_content_root = tkinter.Tk()
#                             prepare_enhance_total_content_root.title('数据整理后续')
#
#                             prepare_enhance_total_content_button = tkinter.Button(prepare_enhance_total_content_root,
#                                                                               text='加法', command=addition_calculation)
#                             prepare_enhance_total_content_button.pack()
#
#                             prepare_enhance_total_content_button1 = tkinter.Button(prepare_enhance_total_content_root,
#                                                                                text='减法',
#                                                                                command=decrease_calculation)
#                             prepare_enhance_total_content_button1.pack()
#
#                             prepare_enhance_total_content_button2 = tkinter.Button(prepare_enhance_total_content_root,
#                                                                                text='乘法',
#                                                                                command=multiplication_calculation)
#                             prepare_enhance_total_content_button2.pack()
#
#                             prepare_enhance_total_content_button3 = tkinter.Button(prepare_enhance_total_content_root,
#                                                                                text='除法',
#                                                                                command=division_calculation)
#                             prepare_enhance_total_content_button3.pack()
#                             prepare_enhance_total_content_root.mainloop()
#
#                 inner_enhance_column_root = tkinter.Tk()
#                 inner_enhance_column_root.title('添加表格数据界面')
#
#                 tkinter.Label(inner_enhance_column_root, text='数量:').grid(row=1, column=0)
#
#                 enhance_num = tkinter.Entry(inner_enhance_column_root)
#                 enhance_num.default_text = '在此输入添加列总数....'
#                 enhance_num.insert(0, enhance_num.default_text)
#                 enhance_num.bind('<FocusIn>', click)
#                 enhance_num.bind('<FocusOut>', out)
#                 enhance_num.grid(row=1, column=1, columnspan=2)
#
#
#                 inner_enhance_column_button = tkinter.Button(inner_enhance_column_root, text='完成添加',
#                                                              command=inner_enhance_column)
#                 inner_enhance_column_button.grid(row=2, column=2)
#                 inner_enhance_column_root.mainloop()
#
#             def reduce_column():
#                 def inner_reduce_column():
#                     print('inner_reduce_column running......')
#                     ensure_delete_column_num = int(delete_column_num.get().strip())
#                     if ensure_delete_column_num <= 0:
#                         messagebox.showwarning('提示', '请输入有效值！')
#                     else:
#                         if messagebox.askyesno('提示',
#                                                f'需要删除的列数为: {ensure_delete_column_num}\n是否进入下一步？'):  # column_title_combine
#                             def prepare_for_delete():
#                                 print('prepare_for_delete running......')
#                                 to_ensure_delete_column_num = list(range(1, ensure_delete_column_num + 1))
#                                 to_ensure_delete = str(ensure_delete.get().strip())
#                                 if to_ensure_delete in column_title_combine1:
#                                     messagebox.showinfo('提示', '查找成功！\n点确定以进行下一步')
#                                     for u in to_ensure_delete_column_num:
#                                         tkinter.Label(prepare_for_delete_root, text='在下方输入删除的相关标题.....')
#                                         tkinter.Label(prepare_for_delete_root, text='标题:').grid(row=u + 1, column=0)
#
#                                         some_need = tkinter.Entry(prepare_for_delete_root)
#                                         some_need.grid(row=u + 1, column=1)
#                                         column_delete_title_combine.append(some_need)
#
#                                     if messagebox.askyesno('提示', '消息保存成功是否进入下一步？'):
#                                         return column_delete_title_combine
#
#                                 else:
#                                     messagebox.showwarning('错误',
#                                                            '你输入的列名\n\d{}\d\n不存在！'.format(to_ensure_delete))
#
#                             prepare_for_delete_root = tkinter.Tk()
#                             prepare_for_delete_root.title('删除详细')
#
#                             som_m_e = str(column_title_combine1).replace('[', '').replace(']', '')
#                             tkinter.Label(prepare_for_delete_root, text=f'当前各列的标题以次为 : {som_m_e}').grid(row=0,
#                                                                                                                   column=2,
#                                                                                                                   columnspan=4)
#                             tkinter.Label(prepare_for_delete_root, text='列名:').grid(row=1, column=0)
#
#                             ensure_delete = tkinter.Entry(prepare_for_delete_root)
#                             ensure_delete.default_text = '在此输入需要删除的列名......'
#                             ensure_delete.insert(0, ensure_delete.default_text)
#                             ensure_delete.bind('<FocusIn>', click)
#                             ensure_delete.bind('<FocusOut>', out)
#                             ensure_delete.grid(row=1, column=1, columnspan=4)
#
#                             prepare_for_delete_button = tkinter.Button(prepare_for_delete_root, text='保存',
#                                                                        command=prepare_for_delete)
#                             prepare_for_delete_button.grid(row=2, column=1)
#                             prepare_for_delete_root.mainloop()
#
#                 inner_reduce_column_root = tkinter.Tk()
#                 inner_reduce_column_root.title('删除表格数据界面')
#
#                 inner_reduce_column_button = tkinter.Button(inner_reduce_column_root, text='next',
#                                                             command=inner_reduce_column)
#                 inner_reduce_column_button.pack()
#
#                 tkinter.Label(inner_reduce_column_root, text='在下方输入需要删除的总列数！').grid(row=0, column=2,
#                                                                                                  columnspan=2)
#                 tkinter.Label(inner_reduce_column_root, text='列数:').grid(row=1, column=0)
#
#                 delete_column_num = tkinter.Entry(inner_reduce_column_root)
#                 delete_column_num.default_text = '在此输入需要删除的总列数......'
#                 delete_column_num.insert(0, delete_column_num.default_text)
#                 delete_column_num.bind('<FocusIn>', click)
#                 delete_column_num.bind('<FocusOut>', out)
#                 delete_column_num.grid(row=1, column=1, columnspan=2)
#                 inner_reduce_column_root.mainloop()
#
#             def click_by_mistakes():
#                 if messagebox.askyesno('提示', '是否退出“表格修改界面”并放弃修改？'):
#                     to_change_column_root.destroy()
#
#             to_change_column_root = tkinter.Tk()
#             to_change_column_root.title('表格修改界面')
#
#             to_change_column_button = tkinter.Button(to_change_column_root, text='添加数据', command=enhance_column)
#             to_change_column_button.pack(side=tkinter.LEFT)
#
#             to_change_column_button1 = tkinter.Button(to_change_column_root, text='退出', command=click_by_mistakes)
#             to_change_column_button1.pack()
#
#             to_change_column_button2 = tkinter.Button(to_change_column_root, text='删除数据', command=reduce_column)
#             to_change_column_button2.pack(side=tkinter.RIGHT)
#             to_change_column_root.mainloop()
#
#         def wanna_quit():
#             if messagebox.askyesno('提示', '确认退出该模式？'):
#                 messagebox.showinfo('提示', '已退出,感谢使用!')
#                 get_origin_data_root.destroy()
#                 get_origin_data_root.quit()
#
#         def to_make_pro_mode_csv():
#             def inner_to_make_pro_mode_csv():
#                 print('inner_to_make_pro_mode_csv running.....')
#                 # to_make_normal_mode_csv  #参考
#                 # column_title_combine1 = []; #参考
#                 # column_row_combine1 = [] #参考
#                 # the_first_mode_data1 = {} #参考
#                 make_csv_info(the_first_mode_data1)
#
#
#             inner_to_make_pro_mode_csv_root = tkinter.Tk()
#             inner_to_make_pro_mode_csv_root.title('表格生成')
#
#             inner_to_make_pro_mode_csv_button = tkinter.Button(inner_to_make_pro_mode_csv_root, text='start',
#                                                                command=inner_to_make_pro_mode_csv)
#             inner_to_make_pro_mode_csv_button.pack()
#             inner_to_make_pro_mode_csv_root.mainloop()
#
#             def qq_uu_ii__tt():
#                 if messagebox.askyesno('提示', '确认退出表格生成界面?'):
#                     to_make_pro_mode_csv_root.destroy()
#
#             to_make_pro_mode_csv_root = tkinter.Tk()
#             to_make_pro_mode_csv_root.title('表格生成操作界面')
#
#             to_make_pro_mode_csv_button = tkinter.Button(to_make_pro_mode_csv_root, text='生成表格',
#                                                          command=inner_to_make_pro_mode_csv)
#             to_make_pro_mode_csv_button.pack()
#
#             to_make_pro_mode_csv_button1 = tkinter.Button(to_make_pro_mode_csv_root, text='退出', command=qq_uu_ii__tt)
#             to_make_pro_mode_csv_button1.pack()
#             to_make_pro_mode_csv_root.mainloop()
#
#         get_origin_data_root = tkinter.Tk()
#         get_origin_data_root.title('增强版')
#
#         tkinter.Label(get_origin_data_root, text='tip:需先输入数据,保存数据后可进行后续操作！').grid(row=0, column=2,
#                                                                                                     columnspan=2)
#         get_origin_data_button = tkinter.Button(get_origin_data_root, text='输入数据', command=get_origin_data)
#         get_origin_data_button.grid(row=1, column=2)
#
#         get_origin_data_button1 = tkinter.Button(get_origin_data_root, text='修改数据', command=to_change_column)
#         get_origin_data_button1.grid(row=2, column=2)
#
#         get_origin_data_button2 = tkinter.Button(get_origin_data_root, text='退出', command=wanna_quit)
#         get_origin_data_button2.grid(row=3, column=2)
#
#         get_origin_data_button3 = tkinter.Button(get_origin_data_root, text='生成表格', command=to_make_pro_mode_csv)
#         get_origin_data_button3.grid(row=4, column=2)
#         get_origin_data_root.mainloop()
#
#
#     def final_version_mode():
#         final_column_title_combine2 = [];final_row_title_combine2 = [];the_first_mode_data2={}
#         ######################################################
#         switch_list = [];row_number_preview = [];new_get_row_content=[]
#         ######################################################
#         def inner_final_version_data():
#             mode_choose_root.destroy()
#             print('prepare_inner_final_version running.....')
#             #####final_version_details####
#             def final_version_original_data():
#                 def inner_final_version_original_data():
#                     print('prepare_inner_final_version running.....')
#                     ask_column = int(final_version_original_data_ask.get().strip())
#                     ask_row = int(final_version_original_data_ask1.get().strip())
#                     if ask_column <= 0:
#                         messagebox.showwarning('提示','输入值无效或错误!')
#                     else:
#                         if messagebox.askyesno('提示','你输入的列数为:{}\n你输入的行数为:{}\n是否继续?'.format(ask_column, ask_row)):
#                             messagebox.showinfo('提示','加载完成,点确认以进入下一步...')
#                             row_number_preview.append(ask_row)
#                             def deal_with_content():
#                                 ask_column_list = list(range(1, ask_column+1))
#                                 ask_row_list = list(range(1, ask_row+1))
#                                 tkinter.Label(deal_with_content_root,text='依次输入各列的标题名和内容！').grid(row=0,column=2,columnspan=3)
#                                 for s in ask_column_list:
#                                     reuse_list = []
#                                     one_title = tkinter.Label(deal_with_content_root,text='标题:')
#                                     one_title.grid(row=s + 2, column=0)
#                                     one_content = tkinter.Entry(deal_with_content_root)
#                                     one_content.default_text = f'在此输入第{s}列的标题名.....'
#                                     one_content.insert(0, one_content.default_text)
#                                     one_content.bind('<FocusIn>',click)
#                                     one_content.bind('<FocusOut>',out)
#                                     one_content.grid(row=s + 2, column=1)
#                                     final_column_title_combine2.append(one_content.get())
#                                     for d in ask_row_list:
#                                         one_row = tkinter.Label(deal_with_content_root,text='行:')
#                                         one_row.grid(row=s + 3 , column= d-1)
#
#                                         one_row_content = tkinter.Entry(deal_with_content_root)
#                                         one_row_content.default_text = '在此输入第{}行的内容....'.format(d)
#                                         one_row_content.insert(0, one_row_content.default_text)
#                                         one_row_content.bind('<FocusIn>',click)
#                                         one_row_content.bind('<FocusOut>',out)
#                                         one_row_content.grid(row=s + 3, column= d)
#                                         reuse_list.append(one_row_content.get())
#                                     final_row_title_combine2.append(reuse_list)
#                                 if messagebox.askyesno('提示','确认储存该数据?'):
#                                     messagebox.showinfo('提示','数据已成功储存!即将返回数据 “处理详细界面”! ')
#                                     deal_with_content_root.destroy()
#                                     # the_first_mode_data1[1111]=1111
#                                     for r in final_column_title_combine2:
#                                         for c in final_row_title_combine2:
#                                             the_first_mode_data2[r] = c
#                                     return final_column_title_combine2, final_row_title_combine2,row_number_preview,the_first_mode_data2
#
#
#                             deal_with_content_root = tkinter.Tk()
#                             deal_with_content_root.title('处理数据')
#
#                             tkinter.Label(deal_with_content_root,text='如完成点击右边按钮....').grid(row=0,column=1,columnspan=3)
#                             tkinter.Label(deal_with_content_root,text='....如完成点击左边按钮').grid(row=0,column=3,columnspan=3)
#
#                             deal_with_content_button = tkinter.Button(deal_with_content_root, text='储存',command=deal_with_content)
#                             deal_with_content_button.grid(row=1,column=2)
#                             deal_with_content_root.mainloop()
#
#
#                 inner_final_version_original_data_root = tkinter.Tk()
#                 inner_final_version_original_data_root.title('获取原始数据')
#
#                 tkinter.Label(inner_final_version_original_data_root,text='需先输入原始数据才可进行筛选!!').grid(row=0, column=2,columnspan=3)
#                 tkinter.Label(inner_final_version_original_data_root,text='列数:').grid(row=1, column=0)
#
#                 final_version_original_data_ask = tkinter.Entry(inner_final_version_original_data_root)
#                 final_version_original_data_ask.default_text = '在此输入需要的列数....'
#                 final_version_original_data_ask.insert(0, final_version_original_data_ask.default_text)
#                 final_version_original_data_ask.bind('<FocusIn>', click)
#                 final_version_original_data_ask.bind('<FocusOut>', out)
#                 final_version_original_data_ask.grid(row=1, column=1)
#
#                 tkinter.Label(inner_final_version_original_data_root,text='行数:').grid(row=2, column=0)
#
#                 final_version_original_data_ask1 = tkinter.Entry(inner_final_version_original_data_root)
#                 final_version_original_data_ask1.default_text = '在此输入各列数需要的行数.....'
#                 final_version_original_data_ask1.insert(0, final_version_original_data_ask1.default_text)
#                 final_version_original_data_ask1.bind('<FocusIn>', click)
#                 final_version_original_data_ask1.bind('<FocusOut>', out)
#                 final_version_original_data_ask1.grid(row=2, column=1)
#
#                 inner_final_version_original_data_button = tkinter.Button(inner_final_version_original_data_root,text='确认',command=inner_final_version_original_data)
#                 inner_final_version_original_data_button.grid(row=3, column=2)
#                 inner_final_version_original_data_root.mainloop()
#
#             def personality_select_option():
#                 print('111')
#                 def make_decrease_for_column():
#                     def inner_decrease_for_column():
#                         print('inner_addition_for_column running....')
#                         to_ensure_something_to_delete = str(ensure_something_to_delete.get().strip())
#                         if to_ensure_something_to_delete not in final_column_title_combine2:
#                             messagebox.showwarning('提示','输入的内容不存在或错误！')
#                         else:
#                             if messagebox.askyesno('提示','确认删除?'):
#                                 for p in final_column_title_combine2:  #转
#                                     if p == to_ensure_something_to_delete:
#                                         continue
#                                     else:
#                                         switch_list.append(p)
#                                 del final_column_title_combine2[:]
#                                 for u in switch_list:
#                                     final_column_title_combine2.append(u)
#
#                                 messagebox.showinfo('提示','你输入的列名:{}已成功删除!'.format(to_ensure_something_to_delete))
#                                 return final_column_title_combine2
#
#                     inner_decrease_for_column_root = tkinter.Tk()
#                     inner_decrease_for_column_root.title('删除列详细')
#
#                     decrease_text = f'{final_column_title_combine2}'.replace('[ ', '').replace(']','')
#                     tkinter.Label(inner_decrease_for_column_root,text=f'当前的列名依次为:{decrease_text}').grid(row=0,column=1,columnspan=3)
#                     tkinter.Label(inner_decrease_for_column_root,text='现在在下面输入待删除的列名').grid(row=1,column=1,columnspan=3)
#                     tkinter.Label(inner_decrease_for_column_root,text='列名:').grid(row=2,column=0)
#
#                     ensure_something_to_delete = tkinter.Entry(inner_decrease_for_column_root)
#                     ensure_something_to_delete.default_text = '在此输入需要删除的列名....'
#                     ensure_something_to_delete.insert(0, ensure_something_to_delete.default_text)
#                     ensure_something_to_delete.bind('<FocusIn>', click)
#                     ensure_something_to_delete.bind('<FocusOut>', out)
#                     ensure_something_to_delete.grid(row=2, column=1,columnspan=3)
#
#                     inner_decrease_for_column_button = tkinter.Button(inner_decrease_for_column_root,text='删除',command=inner_decrease_for_column)
#                     inner_decrease_for_column_button.grid(row=3,column=2)
#                     inner_decrease_for_column_root.mainloop()
#
#                 def make_addition_for_column():
#                     def inner_addition_for_column():
#                         print('inner_addition_for_column running....')
#                         to_ensure_something_to_add = str(ensure_something_to_add.get().strip())
#
#                         if to_ensure_something_to_add in final_column_title_combine2:
#                             if messagebox.askyesno('提示','已存在该列,是否添加?'):
#                                 if messagebox.askyesno('提示','真添加？'):
#                                     final_column_title_combine2.append(to_ensure_something_to_add)
#                         else:
#                             if messagebox.askyesno('提示',f'你输入的待添加列名为:\n{to_ensure_something_to_add}\n是否继续？'):
#                                 final_column_title_combine2.append(to_ensure_something_to_add)
#                         def inner_addition_for_row():
#                             print('inner_addition_for_row running....')
#                             the_row_number_identity = int(row_number_identity.get().strip())
#                             if the_row_number_identity <= 0 or type(the_row_number_identity) == str :
#                                 messagebox.showwarning('提示','输入值无效或错误')
#                             else:
#                                 if messagebox.askyesno('提示','你输入的行数为:{}是否进入下一步?'.format(the_row_number_identity)):
#                                     the_row_number_identity_list = list(range(1,the_row_number_identity+1))
#                                     def something_else():
#                                         print('something_else running....')
#                                         for i in the_row_number_identity_list:
#                                             tkinter.Label(something_else_root,text=f'第{i}行:').grid(row=i,column=0)
#
#                                             t_e_x_t=  tkinter.Entry(something_else_root)
#                                             t_e_x_t.default_text = '在此输入第{}行的内容.....'.format(i)
#                                             t_e_x_t.insert(0,t_e_x_t.default_text)
#                                             t_e_x_t.bind('<FocusIn>', click)
#                                             t_e_x_t.bind('<FocusOut>', out)
#                                             t_e_x_t.grid(row=i,column=1)
#                                             new_get_row_content.append(t_e_x_t.get())
#                                         if messagebox.askyesno('提示','确认输入内容？'):
#                                             final_row_title_combine2.append(new_get_row_content)
#                                             if messagebox.askyesno('提示','数据已成功保存!是否退出当前界面？'):
#                                                 something_else_root.destroy()
#                                                 return final_row_title_combine2
#
#                                     something_else_root = tkinter.Tk()
#                                     something_else_root.title('行数添加详细')
#
#                                     something_else_button = tkinter.Button(something_else_root,text='完成编辑',command=something_else)
#                                     something_else_button.grid(row=the_row_number_identity+1,column=2)
#                                     something_else_root.mainloop()
#
#                         inner_addition_for_row_root = tkinter.Tk()
#                         inner_addition_for_row_root.title('添加行详细')
#
#                         inner_addition_for_row_text = f'当前各列数的行数为{str(row_number_preview).replace('[', '').replace(']', '')}'
#                         tkinter.Label(inner_addition_for_row_root,text=inner_addition_for_row_text).grid(row=1,column=1,columnspan=3)
#                         tkinter.Label(inner_addition_for_row_root,text='行数:').grid(row=2,column=0)
#
#                         row_number_identity = tkinter.Entry(inner_addition_for_row_root)
#                         row_number_identity.default_text = '在此输入需要添加的行数......'
#                         row_number_identity.insert(0, row_number_identity.default_text)
#                         row_number_identity.bind('<FocusIn>', click)
#                         row_number_identity.bind('<FocusOut>', out)
#                         row_number_identity.grid(row=2, column=1,columnspan=3)
#
#                         inner_addition_for_row_button = tkinter.Button(inner_addition_for_row_root,text='下一步',command=inner_addition_for_row)
#                         inner_addition_for_row_button.grid(row=3,column=2)
#                         inner_addition_for_row_root.mainloop()
#
#                     inner_addition_for_column_root = tkinter.Tk()
#                     inner_addition_for_column_root.title('添加列')
#
#                     addition_text = f'{final_column_title_combine2}'.replace('[ ', '').replace(']','')
#                     tkinter.Label(inner_addition_for_column_root,text=f'当前的列名依次为:{addition_text}').grid(row=0,column=1,columnspan=3)
#                     tkinter.Label(inner_addition_for_column_root,text='现在在下面输入待添加的列名').grid(row=1,column=1,columnspan=3)
#                     tkinter.Label(inner_addition_for_column_root,text='列名:').grid(row=2,column=0)
#
#                     ensure_something_to_add = tkinter.Entry(inner_addition_for_column_root)
#                     ensure_something_to_add.default_text= '在此输入需要添加的列名.....'
#                     ensure_something_to_add.insert(0, ensure_something_to_add.default_text)
#                     ensure_something_to_add.bind('<FocusIn>', click)
#                     ensure_something_to_add.bind('<FocusOut>', out)
#                     ensure_something_to_add.grid(row=2, column=1,columnspan=3)
#
#                     inner_addition_for_column_button =tkinter.Button(inner_addition_for_column_root,text='下一步',command=inner_addition_for_column)
#                     inner_addition_for_column_button.grid(row=3,column=2)
#                     inner_addition_for_column_root.mainloop()
#
#
#                 def personality_selection():
#                     print('personality_selection running.....')
#                 personality_selection_root = tkinter.Tk()
#                 personality_selection_root.title('自定义条件设置')
#
#
#                 def personality_select_option_to_quit():
#                     if messagebox.askyesno('提示','确认退出?'):
#                         personality_select_option_root.destroy()
#
#                 personality_select_option_root = tkinter.Tk()
#                 personality_select_option_root.title('数据更改')
#
#                 personality_select_option_button =tkinter.Button(personality_select_option_root,text='添加列',command=make_addition_for_column)
#                 personality_select_option_button.grid(row=2,column=2)
#
#                 personality_select_option_button1 = tkinter.Button(personality_select_option_root,text='删除列',command=make_decrease_for_column)
#                 personality_select_option_button1.grid(row=2,column=5)
#
#                 personality_select_option_button2 = tkinter.Button(personality_select_option_root,text='自定条件',command=personality_selection)
#                 personality_select_option_button2.grid(row=5,column=2)
#
#                 personality_select_option_button3 = tkinter.Button(personality_select_option_root,text='退出',command=personality_select_option_to_quit)
#                 personality_select_option_button3.grid(row=5,column=5)
#                 personality_select_option_root.mainloop()
#
#
#
#             def final_version_details_quit():
#                 if messagebox.askyesno('提示','确认退出?'):
#                     final_version_details_root.destroy()
#
#             final_version_details_root = tkinter.Tk()
#             final_version_details_root.title('数据处理详细界面')
#
#             final_version_details_button = tkinter.Button(final_version_details_root,text='原始数据储存',command=final_version_original_data)
#             final_version_details_button.pack()
#
#             final_version_details_button1 = tkinter.Button(final_version_details_root,text='更改表格',command = personality_select_option )
#             final_version_details_button1.pack()
#
#             final_version_details_button2 = tkinter.Button(final_version_details_root,text='退出',command=final_version_details_quit)
#             final_version_details_button2.pack()
#             final_version_details_root.mainloop()
#
#         def inner_final_version_make_csv():
#             mode_choose_root.destroy()
#             print('inner_final_version running.....')
#             make_csv_info(the_first_mode_data2)
#
#         def inner_version_quit():
#             mode_choose_root.destroy()
#             if messagebox.askyesno('提示','确认退出当前界面?'):
#                 inner_final_version_root.destroy()
#
#         inner_final_version_root = tkinter.Tk()
#         inner_final_version_root.title('增强版(有自定义条件筛选)')
#
#         inner_final_version_button = tkinter.Button(inner_final_version_root, text='数据处理',command=inner_final_version_data)
#         inner_final_version_button.pack()
#
#         inner_final_version_button1 = tkinter.Button(inner_final_version_root,text='生成表格',command=inner_final_version_make_csv)
#         inner_final_version_button1.pack()
#
#         inner_final_version_button2 = tkinter.Button(inner_final_version_root,text='退出',command=inner_version_quit)
#         inner_final_version_button2.pack()
#         inner_final_version_root.mainloop()
#
#     def to_quit():
#         if messagebox.askyesno('提示','是否退出?'):
#             mode_choose_root.destroy()
#             mode_choose_root.quit()
#
#     #####模式总控########
#     mode_choose_root = tkinter.Tk()
#     mode_choose_root.title('功能选择')
#     tkinter.Label(mode_choose_root, text='在下方选择需要的模式....').grid(row=0, column=2, columnspan=3)
#
#     mode_choose_button = tkinter.Button(mode_choose_root, text='一般模式(仅生成)', command=normal_mode)
#     mode_choose_button.grid(row=1, column=2)
#
#     mode_choose_button1 = tkinter.Button(mode_choose_root, text='增强模式(有删减)', command=the_pro_mode)
#     mode_choose_button1.grid(row=2, column=2)
#
#     mode_choose_button3 = tkinter.Button(mode_choose_root, text='最终版', command=final_version_mode)
#     mode_choose_button3.grid(row=3, column=2)
#
#     mode_choose_button2 = tkinter.Button(mode_choose_root,text='退出',command=to_quit)
#     mode_choose_button2.grid(row=4, column=2)
#     mode_choose_root.mainloop()
#
# def to_log():
#     def register():
#         def inner_to_register():
#             first_root.destroy()
#             register_user = str(regis_name.get().strip())
#             register_code = str(regis_code.get().strip())
#             if messagebox.askyesno('提示', '真确认？'):
#                 data_deal.add_user(register_user, register_code)
#                 messagebox.showinfo('注册结果', f'账号已注册成功!/n账号信息为:/n{register_user}/n{register_code}')
#
#         register_root = tkinter.Tk()
#         register_root.title('注册界面')
#
#         tkinter.Label(register_root, text='用户名:').grid(row=0, column=0)
#
#         regis_name = tkinter.Entry(register_root)
#         regis_name.grid(row=0, column=1)
#
#         tkinter.Label(register_root, text='密码:').grid(row=1, column=0)
#
#         regis_code = tkinter.Entry(register_root, show='*')
#         regis_code.grid(row=1, column=1)
#
#         regis_button = tkinter.Button(register_root, text='完成注册', command=inner_to_register)
#         regis_button.grid(row=1, column=2, rowspan=2)
#         register_root.mainloop()
#
#     def login():
#         def inner_to_log():
#             first_root.destroy()
#             input_user_name = str(user_name_type.get().strip())
#             input_user_code = str(user_code_type.get().strip())
#             dealing_name = hashing(input_user_name)
#             dealing_password = hashing(input_user_code)
#             if messagebox.askyesno('提示', '确认？'):
#                 if data_deal.after_data[dealing_name] == dealing_password:
#                     if messagebox.askyesno('提示', '真确认？'):
#                         logging_root.destroy()
#                         messagebox.showinfo('登陆结果', '登陆成功,欢迎使用！用户{}'.format(input_user_name))
#                         ####引用功能总控##########
#                         mode_choose()
#                     else:
#                         if messagebox.askquestion('???', '这账号是你的吗？？'):
#                             messagebox.showinfo('????', '是你的你还不确定？？')
#                         else:
#                             messagebox.showinfo('!!!', '盗号贼坐实了,再见')
#                             logging_root.destroy()
#                 else:
#                     messagebox.showwarning('登录结果', '登录失败,账号或密码错误,请重试！')
#
#         logging_root = tkinter.Tk()
#         logging_root.title('登陆界面')
#
#         tkinter.Label(logging_root, text='若无账号可点击注册以继续.....').grid(row=0, column=2, columnspan=3)
#
#         tkinter.Label(logging_root, text='账号:').grid(row=1, column=0)
#
#         user_name_type = tkinter.Entry(logging_root)
#         user_name_type.default_text = '在此输入账号......'
#         user_name_type.insert(0, user_name_type.default_text)
#         user_name_type.bind('<FocusIn>', click)
#         user_name_type.bind('<FocusOut>', out)
#         user_name_type.grid(row=1, column=1)
#
#         tkinter.Label(logging_root, text='密码:').grid(row=2, column=0)
#
#         user_code_type = tkinter.Entry(logging_root,show='*')
#         user_code_type.grid(row=2, column=1)
#
#         logging_button = tkinter.Button(logging_root, text='下一步', command=inner_to_log)
#         logging_button.grid(row=3, column=2, columnspan=3)
#         logging_root.mainloop()
#
#     def to_quit():
#         if messagebox.askyesno('提示', '确认退出？'):
#             first_root.destroy()
#             first_root.quit()
#
#     first_root = tkinter.Tk()
#     first_root.title('首页')
#
#     to_log_some = tkinter.Button(first_root, text='登录', command=login)
#     to_log_some.pack()
#
#     to_reg_some = tkinter.Button(first_root, text='注册', command=register)
#     to_reg_some.pack()
#
#     to_quit_some = tkinter.Button(first_root, text='退出', command=to_quit)
#     to_quit_some.pack()
#     first_root.mainloop()
# to_log()