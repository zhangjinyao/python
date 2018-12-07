#!/usr/bin/python
#-*- coding:utf-8 -*-
#Author: 白志强
#@Time: 2018/7/13 16:41

from tkinter import *
from tkinter import messagebox
def closeWindow():
    messagebox.showinfo(title='警告', message='不许关闭,好好回答')
    return
def Love():
    love = Toplevel(window)
    love.geometry("300x100+520+260")
    love.title("好巧，我也是")
    label = Label(love, text="好巧，我也是", font=("微软雅黑", 20))
    label.pack()
    btn = Button(love, text="确定", width=10, height=2, command=closeallwindow)
    btn.pack()
    love.protocol('WM_DELETE_WINDOW', closelove)
def closelove():
    messagebox.showinfo(title='哈哈哈', message='刚好，我也是')
    return
def closeallwindow():
    window.destroy()
def NoLove():
    no_love = Toplevel(window)
    no_love.geometry("300x100+520+260")
    no_love.title("再考虑考虑")
    label = Label(no_love, text="想清楚再说", font=("微软雅黑", 20))
    label.pack()
    btn = Button(no_love, text="好的", width=10,
                 height=2, command=no_love.destroy)
    btn.pack()
    no_love.protocol('WM_DELETE_WINDOW', closenolove)
def closenolove():
    NoLove()
window = Tk()
window.title("你喜欢我吗？")
window.geometry("380x420+300+240")
window.protocol('WM_DELETE_WINDOW', closeWindow)
label = Label(window, text='hey,小姐姐', font=("微软雅黑", 15))
label.grid(row=0, column=0)
label1 = Label(window, text="喜欢我吗？", font=("微软雅黑", 30))
label1.grid(row=1, column=1, sticky=E)
btn = Button(window, text="喜欢", width=15, height=2, command=Love)
btn.grid(row=3, column=0, sticky=W)
btn1 = Button(window, text="不喜欢", command=NoLove)
btn1.grid(row=3, column=1, sticky=E)
window.mainloop()

