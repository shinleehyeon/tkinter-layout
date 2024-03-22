
from tkinter import Tk, PanedWindow, Menu, LabelFrame
from tkinter.ttk import Label, Entry, Button, Radiobutton
from tkinter import *
import tkinter as tk


win = Tk()
win.geometry('1000x1000')
win.title("법규")
menu_area = Menu(win)
win.configure(menu=menu_area)


menu1 = Menu(menu_area)
#menu1.add_command(label="New...")
menu_area.add_cascade(menu=menu1)

label_frame = LabelFrame(win, text='시세정보')
label_frame.grid(row=0, column=0, padx=5, pady=5)

lbl_a = Label(label_frame, text="현재가격:")
lbl_b = Label(label_frame, text="매수가격:")
lbl_c = Label(label_frame, text="보유코인:")
lbl_d = Label(label_frame, text="계좌잔고:")
lbl_e = Label(label_frame, text="계좌평가:")
lbl_f = Label(label_frame, text="누적수익율:")
lbl_g = Label(label_frame, text="누적수익금:")

entry_a = Entry(label_frame)
entry_b = Entry(label_frame)
entry_c = Entry(label_frame)
entry_d = Entry(label_frame)
entry_e = Entry(label_frame)
entry_f = Entry(label_frame)
entry_g = Entry(label_frame)


lbl_a.grid(row=0, column=0)
entry_a.grid(row=0, column=1, padx=5, pady=5)
lbl_b.grid(row=1, column=0)
entry_b.grid(row=1, column=1, padx=5, pady=5)
lbl_c.grid(row=2, column=0)
entry_c.grid(row=2, column=1, padx=5, pady=5)
lbl_d.grid(row=3, column=0)
entry_d.grid(row=3, column=1, padx=5, pady=5)
lbl_e.grid(row=4, column=0)
entry_e.grid(row=4, column=1, padx=5, pady=5)
lbl_f.grid(row=5, column=0)
entry_f.grid(row=5, column=1, padx=5, pady=5)
lbl_g.grid(row=6, column=0)
entry_g.grid(row=6, column=1, padx=5, pady=5)



str = StringVar()
#
Radiovar = IntVar()
#
label_frae = LabelFrame(win, text='구분')
label_frae.grid(row=10, column=0, padx=5, pady=5)
#
Radio_Button3 = Radiobutton(label_frae, text="운영", variable=Radiovar, value=1)
Radio_Button2 = Radiobutton(label_frae, text="백테스팅", variable=Radiovar, value=2)
#
entry_button3 = Entry(label_frame)
entry_button2 = Entry(label_frame)

Radio_Button3.grid(row=0, column=0)
entry_button3.grid(row=0, column=1)
Radio_Button2.grid(row=0, column=108)
entry_button2.grid(row=0, column=1)


st = StringVar()
#
Radiova = IntVar()
#
label_fra = LabelFrame(win, text='API 구분')
label_fra.grid(row=20, column=0, padx=1, pady=1)
#
Radio_Button1 = Radiobutton(label_fra, text="실매매", variable=Radiova, value=1)
Radio_Button4 = Radiobutton(label_fra, text="테스팅", variable=Radiova, value=2)
#
entry_button1 = Entry(label_frame)
entry_button4 = Entry(label_frame)

Radio_Button1.grid(row=0, column=1)
entry_button1.grid(row=0, column=1)
Radio_Button4.grid(row=0, column=420)
entry_button4.grid(row=0, column=1)

def btnEvtHandler() :
    print("버튼이 클릭 되었습니다!")
    #value = entry.get()
    #lbl.config(text="성명 : " + value)



panedwindow=PanedWindow(relief="raised", bd=0)
panedwindow.grid(row=30,column=0, columnspan=20, padx=5, pady=5)
btn_ok = Button(panedwindow, text="Start", command=btnEvtHandler)
btn_cancel = Button(panedwindow, text="Stop", command=btnEvtHandler)

panedwindow.add(btn_ok)
panedwindow.add(btn_cancel)



OptionList = [
"A",
"B",
"C",
"D"
]



#
#
variable = StringVar(win)
variable.set(OptionList[0])

opt = OptionMenu(win, variable, *OptionList)
opt.config(width=9, font=('Helvetica', 10))
opt.grid()

win.mainloop()
opt = OptionMenu(app, variable, *OptionList)


if __name__ == '__main__':
    win.mainloop()