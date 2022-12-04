import ctypes
import os

DIR = os.path.dirname(os.path.abspath(__file__))
DLL_PATH = os.path.join(DIR, 'libexdui.dll')
EXT_PATH = os.path.join(DIR, 'Default.ext')

ExDUIR = ctypes.CDLL(DLL_PATH)

EXGF_RENDER_METHOD_D2D = 0x100  # 引擎标识_渲染_使用D2D
EXGF_OBJECT_SHOWRECTBORDER = 0x20000  # 引擎标识_组件_显示组件边界

EWS_BUTTON_CLOSE = 0x01  # 窗体风格_关闭按钮
EWS_BUTTON_MAX = 0x02  # 窗体风格_最大化按钮
EWS_BUTTON_MIN = 0x04  # 窗体风格_最小化按钮
EWS_HASICON = 0x80  # 窗体风格_图标
EWS_TITLE = 0x100  # 窗体风格_标题
EWS_SIZEABLE = 0x400  # 窗体风格_允许调整尺寸
EWS_MOVEABLE = 0x800  # 窗体风格_允许随意移动
EWS_MAINWINDOW = 0x10000  # 窗体风格_主窗口
EWS_CENTERWINDOW = 0x20000  # 窗体风格_窗口居中

EWL_BLUR = -2  # 引擎数值_背景模糊
EWL_ALPHA = -5  # 引擎数值_窗口透明度
EWL_CRBORDER = -30  # 引擎数值_边框颜色
EWL_CRBKG = -31  # 引擎数值_背景颜色

COLOR_EX_BACKGROUND = 0  # 颜色索引_背景颜色
COLOR_EX_BORDER = 1  # 颜色索引_边框颜色
COLOR_EX_TEXT_NORMAL = 2  # 颜色索引_文本颜色_正常
COLOR_EX_TEXT_HOVER = 3  # 颜色索引_文本颜色_点燃
COLOR_EX_TEXT_DOWN = 4  # 颜色索引_文本颜色_按下

NM_CLICK = -2  # 事件_左键被单击
NM_DBLCLK = -3  # 事件_左键被双击
NM_RCLICK = -5  # 事件_右键被单击

DT_TOP = 0x00000000  # 文本格式_顶对齐
DT_LEFT = 0x00000000  # 文本格式_左对齐
DT_CENTER = 0x00000001  # 文本格式_水平居中
DT_RIGHT = 0x00000002  # 文本格式_右对齐
DT_VCENTER = 0x00000004  # 文本格式_垂直居中
DT_BOTTOM = 0x00000008  # 文本格式_底对齐
DT_WORDBREAK = 0x00000010  # 文本格式_自动换行
DT_SINGLELINE = 0x00000020  # 文本格式_单行模式

EOS_VISIBLE = 0x10000000  # 组件风格_可视
EOS_VSCROLL = 0x40000000  # 组件风格_垂直滚动条
EOS_HSCROLL = 0x80000000  # 组件风格_水平滚动条

EES_USEPASSWORD = 0x02  # 编辑框风格_密码输入
EES_READONLY = 0x20  # 编辑框风格_只读
EES_NUMERICINPUT = 0x80  # 编辑框风格_数值输入


def lobyte(w):
    return w & 0xff


def hibyte(w):
    return (w >> 8) & 0xff


def loword(l):
    return l & 0xffff


def hiword(l):
    return (l >> 16) & 0xffff


def ex_get_red(argb: int) -> int:
    return lobyte(argb)


def ex_get_green(argb) -> int:
    return lobyte(argb >> 8)


def ex_get_blue(argb: int) -> int:
    return lobyte(argb >> 16)


def ex_get_alpha(argb: int) -> int:
    return lobyte(argb >> 24)


def ex_rgb(red: int, green: int, blue: int) -> int:
    return red | green << 8 | blue << 16


def ex_rgba(red: int, green: int, blue: int, alpha: int) -> int:
    return ex_rgb(red, green, blue) | alpha << 24


def ex_rgb_to_rgba(rgb: int, alpha: int) -> int:
    return ex_get_red(rgb) << 16 | ex_get_green(rgb) << 8 | ex_get_blue(rgb) | alpha << 24


def ex_init(flag: int = EXGF_RENDER_METHOD_D2D) -> bool:
    with open(EXT_PATH, 'rb') as f:
        ext = f.read()
    return ExDUIR.Ex_Init(0, flag, 0, 0, ext, len(ext), 0, 0)


def ex_wnd_create(parent: int, title: str, left: int, top: int, width: int, height: int) -> int:
    return ExDUIR.Ex_WndCreate(parent, 0, title, left, top, width, height, 0, 0)


def ex_dui_bind_window_ex(hwnd: int, style: int, lparam: int, msgproc: int) -> int:
    return ExDUIR.Ex_DUIBindWindowEx(hwnd, 0, style, lparam, msgproc)


def ex_dui_show_window(hexdui: int) -> bool:
    return ExDUIR.Ex_DUIShowWindow(hexdui, 1, 0, 0)


def ex_wnd_msg_loop() -> int:
    return ExDUIR.Ex_WndMsgLoop()


def ex_uninit():
    ExDUIR.Ex_UnInit()


def ex_dui_set_long(hexdui: int, index: int, long: int) -> int:
    return ExDUIR.Ex_DUISetLong(hexdui, index, long)


def ex_obj_create(class_name: str, title: str, style: int, x: int, y: int, width: int, height: int, parent: int) -> int:
    return ExDUIR.Ex_ObjCreate(class_name, title, style, x, y, width, height, parent)


def ex_obj_create_ex(style_ex: int, class_name: str, title: str, style: int, x: int, y: int, width: int, height: int, parent: int, id: int, text_format: int, lparam: int, msg_proc: int) -> int:
    return ExDUIR.Ex_ObjCreateEx(style_ex, class_name, title, style, x, y, width, height, parent, id, text_format, lparam, 0, msg_proc)


def ex_obj_set_background_image(handle: int, image, image_len: int, x: int, y: int, repeat: int, flags: int, alpha: int, update: bool) -> bool:
    return ExDUIR.Ex_ObjSetBackgroundImage(handle, image, image_len, x, y, repeat, 0, flags, alpha, update)


def ex_obj_handle_event(hobj: int, event: int, callback: int) -> bool:
    return ExDUIR.Ex_ObjHandleEvent(hobj, event, callback)


def ex_obj_set_color(hobj: int, index: int, color: int, redraw: bool) -> int:
    return ExDUIR.Ex_ObjSetColor(hobj, index, color, redraw)


def ex_messagebox(handle: int, text: str, caption: str, utype: int, flags: int) -> int:
    return ExDUIR.Ex_MessageBox(handle, text, caption, utype, flags)


def ex_obj_set_text(hobj: int, text: str, redraw: bool) -> bool:
    return ExDUIR.Ex_ObjSetText(hobj, text, redraw)


def ex_obj_get_text_length(hobj: int) -> int:
    return ExDUIR.Ex_ObjGetTextLength(hobj)


def ex_obj_get_text(hobj: int) -> str:
    text_len = ex_obj_get_text_length(hobj)*2
    ret_str = ''
    ret_str.zfill(text_len+2)
    ret = ctypes.c_wchar_p(ret_str)
    ExDUIR.Ex_ObjGetText(hobj, ret, text_len)
    return ret.value
