from exduir import *
from ctypes import *
# import tkinter as tk
# from tkinter import filedialog

@ctypes.PYFUNCTYPE(c_longlong,c_size_t,c_int,c_int,c_size_t,c_size_t,c_void_p)
def msg_proc(hwnd:int,handle:int,umsg:int,wparam:int,lparam:int,lpresult:int)->int:
    # if umsg==5:
    #     print('改变窗口大小消息',umsg)
    return 0

@ctypes.PYFUNCTYPE(c_longlong,c_int,c_int,c_int,c_size_t,c_size_t)
def on_button_event(hobj:int,id:int,code:int,wparam:int,lparam:int)->int:
    if code==NM_CLICK:
        if hobj==hobj_button1:
            #answer='text1'
            print('create')
            # application_window = tk.Tk()
            print('create1')
            # application_window.withdraw()
            print('create2')
            # answer = filedialog.askopenfilename(parent=application_window,
            #                             initialdir=os.getcwd(),
            #                             title="Please select a file:",
            #                             filetypes= [('all files', '.*'), ('text files', '.txt')])
            # print('create3')
            # ex_obj_set_text(hobj_edit1,answer,False)
            # application_window.destroy()
        elif hobj==hobj_button2:
            # application_window = tk.Tk()
            # application_window.withdraw()
            # answer = filedialog.askopenfilename(parent=application_window,
            #                             initialdir=os.getcwd(),
            #                             title="Please select a file:",
            #                             filetypes= [('all files', '.*'), ('text files', '.txt')])
            answer='text2'
            print(answer,len(answer))
            ex_obj_set_text(hobj_edit2,answer,False)
        elif hobj==hobj_button3:
            text_edit1=ex_obj_get_text(hobj_edit1)
            #text_edit2=ex_obj_get_text(hobj_edit2)
            print(text_edit1)
            #ex_messagebox(hexdui,text_edit2,text_edit1,0,0)
    return 0

ex_init()
hwnd=ex_wnd_create(0,'test',0,0,500,500)
hexdui=ex_dui_bind_window_ex(hwnd,EWS_MAINWINDOW | EWS_BUTTON_CLOSE | EWS_BUTTON_MIN  |  EWS_BUTTON_MAX | EWS_MOVEABLE | EWS_CENTERWINDOW | EWS_TITLE | EWS_SIZEABLE | EWS_HASICON,0,msg_proc)
ex_dui_set_long(hexdui,EWL_CRBKG,ex_rgba(150,150,150,255))

hobj_button1=ex_obj_create('button','按钮1',-1,10,50,100,30,hexdui)
ex_obj_handle_event(hobj_button1,NM_CLICK,on_button_event)

hobj_edit1=ex_obj_create('edit','',-1,110,50,200,30,hexdui)

hobj_button2=ex_obj_create('button','按钮2',-1,10,90,100,30,hexdui)
ex_obj_handle_event(hobj_button2,NM_CLICK,on_button_event)

hobj_edit2=ex_obj_create('edit','',-1,110,90,200,30,hexdui)

hobj_button3=ex_obj_create('button','按钮3',-1,10,130,100,30,hexdui)
ex_obj_handle_event(hobj_button3,NM_CLICK,on_button_event)


ex_dui_show_window(hexdui)
ex_wnd_msg_loop()
ex_uninit()