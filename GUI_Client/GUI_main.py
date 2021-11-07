import tkinter as tk
from PIL import Image, ImageTk

import client2
import Db_handler

host = "127.0.0.1"
port = 20001
BUFFER_SIZE = 1940
client = client2.ConnectServer(host, port)
Data_Object = Db_handler.Db_handler(client)

titlename = '主視窗'



GUI_main = tk.Tk()
GUI_main.title(titlename)
GUI_main.resizable(0,0)#固定視窗大小
align_mode = 'nswe'#置中
pad = 5

div_size = 200
img_size = div_size * 2
div_mainspace = tk.Frame(GUI_main,  width=img_size , height=img_size , bg='blue')
div_title = tk.Frame(GUI_main,  width=div_size , height=div_size , bg='orange')
div_bt = tk.Frame(GUI_main,  width=div_size , height=div_size , bg='green')


def AddWorker():

    def execute():
        target_ID = int(Employee_ID_entry.get())
        Name = Employee_Name_entry.get()
        Shift = int(Employee_shift_entry.get())
        Rate = int(Employee_rate_entry.get())
        #print(Data_Object.Check_if_exist(target_ID))
        if(Data_Object.Check_if_exist(target_ID)):
            result = '此ID已經存在!'
        else:
            Data_Object.add_modify_employee(Name, target_ID, 1, Shift, Rate)
            result = '新增成功!'
        #print(result)
        result_label.configure(text=result)

    GUI_add = tk.Toplevel(GUI_main)
    GUI_add.title('新增工讀')
    GUI_add.resizable(0,0)#固定視窗大小

    Employee_ID_frame = tk.Frame(GUI_add)
    Employee_ID_frame.pack(side=tk.TOP)
    Employee_ID_label = tk.Label(Employee_ID_frame, text='員工ＩＤ:')
    Employee_ID_label.pack(side=tk.LEFT)
    Employee_ID_entry = tk.Entry(Employee_ID_frame)
    Employee_ID_entry.pack(side=tk.LEFT)

    Employee_Name_frame = tk.Frame(GUI_add)
    Employee_Name_frame.pack(side=tk.TOP)
    Employee_Name_label = tk.Label(Employee_Name_frame, text='員工姓名:')
    Employee_Name_label.pack(side=tk.LEFT)
    Employee_Name_entry = tk.Entry(Employee_Name_frame)
    Employee_Name_entry.pack(side=tk.LEFT)

    Employee_shift_frame = tk.Frame(GUI_add)
    Employee_shift_frame.pack(side=tk.TOP)
    Employee_shift_label = tk.Label(Employee_shift_frame, text='日(1)/夜(2)班:')
    Employee_shift_label.pack(side=tk.LEFT)
    Employee_shift_entry = tk.Entry(Employee_shift_frame)
    Employee_shift_entry.pack(side=tk.LEFT)

    Employee_rate_frame = tk.Frame(GUI_add)
    Employee_rate_frame.pack(side=tk.TOP)
    Employee_rate_label = tk.Label(Employee_rate_frame, text='時　薪　:')
    Employee_rate_label.pack(side=tk.LEFT)
    Employee_rate_entry = tk.Entry(Employee_rate_frame)
    Employee_rate_entry.pack(side=tk.LEFT)

    result_label = tk.Label(GUI_add)
    result_label.pack()
    

    calculate_btn = tk.Button(GUI_add, text='送出',command = execute)
    calculate_btn.pack()

def AddSupervisor():

    def execute():
        target_ID = int(Employee_ID_entry.get())
        Name = Employee_Name_entry.get()
        salary = int(Employee_salary_entry.get())
        bonus = int(Employee_bonus_entry.get())
        if(Data_Object.Check_if_exist(target_ID)):
            result = '此ID已經存在!'
        else:
            Data_Object.add_modify_employee(Name, target_ID, 1, salary, bonus)
            result = '新增成功!'
        result_label.configure(text=result)

    GUI_add = tk.Toplevel(GUI_main)
    GUI_add.title('新增正職')
    GUI_add.resizable(0,0)#固定視窗大小

    Employee_ID_frame = tk.Frame(GUI_add)
    Employee_ID_frame.pack(side=tk.TOP)
    Employee_ID_label = tk.Label(Employee_ID_frame, text='員工ＩＤ:')
    Employee_ID_label.pack(side=tk.LEFT)
    Employee_ID_entry = tk.Entry(Employee_ID_frame)
    Employee_ID_entry.pack(side=tk.LEFT)

    Employee_Name_frame = tk.Frame(GUI_add)
    Employee_Name_frame.pack(side=tk.TOP)
    Employee_Name_label = tk.Label(Employee_Name_frame, text='員工姓名:')
    Employee_Name_label.pack(side=tk.LEFT)
    Employee_Name_entry = tk.Entry(Employee_Name_frame)
    Employee_Name_entry.pack(side=tk.LEFT)

    Employee_salary_frame = tk.Frame(GUI_add)
    Employee_salary_frame.pack(side=tk.TOP)
    Employee_salary_label = tk.Label(Employee_salary_frame, text='薪　資　:')
    Employee_salary_label.pack(side=tk.LEFT)
    Employee_salary_entry = tk.Entry(Employee_salary_frame)
    Employee_salary_entry.pack(side=tk.LEFT)

    Employee_bonus_frame = tk.Frame(GUI_add)
    Employee_bonus_frame.pack(side=tk.TOP)
    Employee_bonus_label = tk.Label(Employee_bonus_frame, text='獎　金　:')
    Employee_bonus_label.pack(side=tk.LEFT)
    Employee_bonus_entry = tk.Entry(Employee_bonus_frame)
    Employee_bonus_entry.pack(side=tk.LEFT)


    result_label = tk.Label(GUI_add)
    result_label.pack()
    

    calculate_btn = tk.Button(GUI_add, text='送出',command = execute)
    calculate_btn.pack()

def Get_all_employee():
    Data_Object.list_all_employee()
    Massages = Data_Object.Massages
    
    GUI_Get_all = tk.Toplevel(GUI_main)
    GUI_Get_all.title('所有ＩＤ')
    GUI_Get_all.resizable(0,0)#固定視窗大小
    #Employee_ID_frame = tk.Frame(GUI_Get_all)
    
    result_label = tk.Label(GUI_Get_all)
    result_label.pack()
    result_label.configure(text=Massages)

def SearchEmployee():

    def execute():
        target_ID = int(Employee_ID_entry.get())
        if(Data_Object.Check_if_exist(target_ID)):
            Data_Object.look_up_employee(target_ID)
            result = Data_Object.reply_msg
        else:
            result = '此ID不存在!'
        result_label.configure(text=result)

    GUI_search = tk.Toplevel(GUI_main)
    GUI_search.title('搜尋ＩＤ')
    GUI_search.resizable(0,0)#固定視窗大小

    Employee_ID_frame = tk.Frame(GUI_search)
    Employee_ID_frame.pack(side=tk.TOP)
    Employee_ID_label = tk.Label(Employee_ID_frame, text='搜尋ＩＤ:')
    Employee_ID_label.pack(side=tk.LEFT)
    Employee_ID_entry = tk.Entry(Employee_ID_frame)
    Employee_ID_entry.pack(side=tk.LEFT)

    result_label = tk.Label(GUI_search)
    result_label.pack()
    

    calculate_btn = tk.Button(GUI_search, text='送出',command = execute)
    calculate_btn.pack()
    

def DeleteEmployee():
    def execute():
        target_ID = int(Employee_ID_entry.get())
        if(Data_Object.Check_if_exist(target_ID)):
            Data_Object.del_employee(target_ID)
            result = '刪除成功!'
        else:
            result = '此ID不存在!'
        result_label.configure(text=result)

    GUI_Delete = tk.Toplevel(GUI_main)
    GUI_Delete.title('刪除ＩＤ')
    GUI_Delete.resizable(0,0)#固定視窗大小

    Employee_ID_frame = tk.Frame(GUI_Delete)
    Employee_ID_frame.pack(side=tk.TOP)
    Employee_ID_label = tk.Label(Employee_ID_frame, text='刪除ＩＤ:')
    Employee_ID_label.pack(side=tk.LEFT)
    Employee_ID_entry = tk.Entry(Employee_ID_frame)
    Employee_ID_entry.pack(side=tk.LEFT)

    result_label = tk.Label(GUI_Delete)
    result_label.pack()
    

    calculate_btn = tk.Button(GUI_Delete, text='送出',command = execute)
    calculate_btn.pack()
        



def define_layout(obj, cols=1, rows=1):
    
    def method(trg, col, row):
        
        for c in range(cols):    
            trg.columnconfigure(c, weight=1)
        for r in range(rows):
            trg.rowconfigure(r, weight=1)

    if type(obj)==list:        
        [ method(trg, cols, rows) for trg in obj ]
    else:
        trg = obj
        method(trg, cols, rows)


"""
Getall = Get_all_employee(Data_Object)
Search = SearchEmployee(Data_Object)
Delete = DeleteEmployee(Data_Object)
"""


GUI_main.update()
win_size = min( GUI_main.winfo_width(), GUI_main.winfo_height())
#print(win_size)

div_mainspace.grid(column=0, row=0, padx=pad, pady=pad, rowspan=2, sticky=align_mode)
div_title.grid(column=1, row=0, padx=pad, pady=pad, sticky=align_mode)
div_bt.grid(column=1, row=1, padx=pad, pady=pad, sticky=align_mode)

define_layout(GUI_main, cols=2, rows=2)
define_layout([div_mainspace, div_title, div_bt])

im = Image.open('./GUI_Client/10_brown.png')
imTK = ImageTk.PhotoImage( im.resize( (img_size, img_size) ) )

image_main = tk.Label(div_mainspace, image=imTK)
image_main['height'] = img_size
image_main['width'] = img_size

image_main.grid(column=0, row=0, sticky=align_mode)

lbl_title1 = tk.Label(div_title, text='操作', bg='orange', fg='white')
lbl_title2 = tk.Label(div_title, text="介面", bg='orange', fg='white')

lbl_title1.grid(column=0, row=0, sticky=align_mode)
lbl_title2.grid(column=0, row=1, sticky=align_mode)

bt_addW = tk.Button(div_bt, text='新增工讀', bg='green', fg='white',command=AddWorker)
bt_addS = tk.Button(div_bt, text='新增正職', bg='green', fg='white',command=AddSupervisor)
bt_ls = tk.Button(div_bt, text='列出所有', bg='green', fg='white',command=Get_all_employee)
bt_lkup = tk.Button(div_bt, text='查詢員工', bg='green', fg='white',command=SearchEmployee)
bt_del = tk.Button(div_bt, text='刪除員工', bg='green', fg='white',command=DeleteEmployee)

bt_addW.grid(column=0, row=0, sticky=align_mode)
bt_addS.grid(column=0, row=1, sticky=align_mode)
bt_ls.grid(column=0, row=2, sticky=align_mode)
bt_lkup.grid(column=0, row=3, sticky=align_mode)
bt_del.grid(column=0, row=4, sticky=align_mode)


define_layout(GUI_main, cols=2, rows=2)
define_layout(div_mainspace)
define_layout(div_title, rows=2)
define_layout(div_bt, rows=5)


GUI_main.mainloop()