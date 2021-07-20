from tkinter import *
root = Tk()
root.geometry("250x400")
root.title("Calculator")
bg_color = "#ffffcc"
title = Label(root, text="calculator", bd = 10,bg=bg_color, fg="black", font = ("time new roman",15,"bold")).pack(fill=X)

def btn_click(item):
    global expression
    expression = expression + str(item)
    input_text.set(expression)

def bt_clear(): 
    global expression 
    expression = "" 
    input_text.set("")

def bt_equal():
    global expression
    result = str(eval(expression)) # 'eval':This function is used to evaluates the string expression directly
    input_text.set(result)
    expression = ""
 
expression = ""
 
input_text = StringVar()
 
entry_area = Entry(root, width=21, font="arial 15", bd=7,relief = SUNKEN, textvariable=input_text)
entry_area.place(x = 0, y=50)
btn = Label(root, width= 26, bd=7)
btn.place(x = 0, y=90)

#-------------------fist row button------------------
btn_1 = Button(btn, text="7",width = 2,font=("time new roman", 15, "bold"),bg=bg_color, fg = "black", bd = 12, relief = GROOVE, command = lambda: btn_click("7")).grid(row = 0, column=0, padx = 1, pady=5)
btn_2 = Button(btn, text="8",width = 2,font=("time new roman", 15, "bold"),bg=bg_color, fg = "black", bd = 12, relief = GROOVE, command = lambda: btn_click("8")).grid(row = 0, column=1, padx = 1, pady=5)
btn_3 = Button(btn, text="9",width = 2,font=("time new roman", 15, "bold"),bg=bg_color, fg = "black", bd = 12, relief = GROOVE, command = lambda: btn_click("9")).grid(row = 0, column=2, padx = 1, pady=5)
btn_4 = Button(btn, text="/",width = 2,font=("time new roman", 15, "bold"),bg=bg_color, fg = "black", bd = 12, relief = GROOVE, command = lambda: btn_click("/")).grid(row = 0, column=3, padx = 1, pady=5)

#-------------------second row button-----------------------------
btn_5 = Button(btn, text="4",width = 2,font=("time new roman", 15, "bold"),bg=bg_color, fg = "black", bd = 12, relief = GROOVE, command = lambda: btn_click("4")).grid(row = 1, column=0, padx = 7, pady=5)
btn_6 = Button(btn, text="5",width = 2,font=("time new roman", 15, "bold"),bg=bg_color, fg = "black", bd = 12, relief = GROOVE, command = lambda: btn_click("5")).grid(row = 1, column=1, padx = 2, pady=5)
btn_7 = Button(btn, text="6",width = 2,font=("time new roman", 15, "bold"),bg=bg_color, fg = "black", bd = 12, relief = GROOVE, command = lambda: btn_click("6")).grid(row = 1, column=2, padx = 2, pady=5)
btn_8 = Button(btn, text="*",width = 2,font=("time new roman", 15, "bold"),bg=bg_color, fg = "black", bd = 12, relief = GROOVE, command = lambda: btn_click("*")).grid(row = 1, column=3, padx = 2, pady=5)

#----------------------third row button------------------------------
btn_9 = Button(btn, text="1",width = 2,font=("time new roman", 15, "bold"),bg=bg_color, fg = "black", bd = 12, relief = GROOVE, command = lambda: btn_click("1")).grid(row = 2, column=0, padx = 7, pady=5)
btn_10 = Button(btn, text="2",width = 2,font=("time new roman", 15, "bold"),bg=bg_color, fg = "black", bd = 12, relief = GROOVE, command = lambda: btn_click("2")).grid(row = 2, column=1, padx = 2, pady=5)
btn_11 = Button(btn, text="3",width = 2,font=("time new roman", 15, "bold"),bg=bg_color, fg = "black", bd = 12, relief = GROOVE, command = lambda: btn_click("3")).grid(row = 2, column=2, padx = 2, pady=5)
btn_12 = Button(btn, text="-",width = 2,font=("time new roman", 15, "bold"),bg=bg_color, fg = "black", bd = 12, relief = GROOVE, command = lambda: btn_click("-")).grid(row = 2, column=3, padx = 2, pady=5)

#----------------------fourth row button--------------------------------
btn_13 = Button(btn, text="+",width = 2,font=("time new roman", 15, "bold"),bg=bg_color, fg = "black", bd = 12, relief = GROOVE, command = lambda: btn_click("+")).grid(row = 3, column=0, padx = 7, pady=5)
btn_14 = Button(btn, text="0",width = 2,font=("time new roman", 15, "bold"),bg=bg_color, fg = "black", bd = 12, relief = GROOVE, command = lambda: btn_click("0")).grid(row = 3, column=1, padx = 2, pady=5)
btn_15 = Button(btn, text="c",width = 2,font=("time new roman", 15, "bold"),bg=bg_color, fg = "black", bd = 12, relief = GROOVE, command = lambda: bt_clear()).grid(row = 3, column=2, padx = 2, pady=5)
btn_16 = Button(btn, text="=",width = 2,font=("time new roman", 15, "bold"),bg=bg_color, fg = "black", bd = 12, relief = GROOVE, command = lambda: bt_equal()).grid(row = 3, column=3, padx = 2, pady=5)
root.mainloop()