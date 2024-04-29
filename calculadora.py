from tkinter import *
from tkinter import ttk

#colors

color1 = "#1e1f1e" # black
color2 = "#feffff" # white
color3 = "navy" # blue
color4 = "light grey" # gray
color5 = "orange" # orange

#window

window = Tk()
window.title("Calculator")
window.geometry("235x308")
window.config(background=color1) # can be either bg or background 

#calculator's top part

top_frame = Frame(window, width=235, height=50, background=color3)
top_frame.grid(row=0, column=0)

#Body

body_frame = Frame(window, width=235, height=268)
body_frame.grid(row=1, column=0)

# all values variable

all_values = ''

#Creating a function:
value_text = StringVar()

def enter_values(event):

    global all_values

    all_values = all_values + str(event)

    #passing value to the screen
    value_text.set(all_values)

#function to calculate
def calculate():
    result = eval(all_values)
    
    value_text.set(str(result))

def clear_screen():
    global all_values
    all_values = ""
    value_text.set("")

#Creating a Label:

app_label = Label(top_frame, textvariable=value_text, width=15, height=2, relief=FLAT, anchor="e", justify=RIGHT, font=('Ivy 18 bold'), bg=color3, fg=color2, wraplength=200)
app_label.place(x=0, y=0)

#buttons

#First Row:

btn_1 = Button(body_frame, command=clear_screen, text="C", width=11, height=2, bg=color4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
btn_1.place(x=0, y=0)

btn_2 = Button(body_frame, command=lambda: enter_values('%'), text="%", width=5, height=2, bg=color4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
btn_2.place(x=118, y=0)

btn_3 = Button(body_frame, command=lambda: enter_values('/'), text="/", width=5, height=2, bg=color5, fg=color2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
btn_3.place(x=177, y=0)

#Second Row:

btn_4 = Button(body_frame, command=lambda: enter_values('7'), text="7", width=5, height=2, bg=color4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
btn_4.place(x=0, y=52)

btn_5 = Button(body_frame, command=lambda: enter_values('8'), text="8", width=5, height=2, bg=color4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
btn_5.place(x=59, y=52)

btn_6 = Button(body_frame, command=lambda: enter_values('9'), text="9", width=5, height=2, bg=color4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
btn_6.place(x=118, y=52)

btn_7 = Button(body_frame, command=lambda: enter_values('*'), text="*", width=5, height=2, bg=color5, fg=color2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
btn_7.place(x=177, y=52)

#Third Row:

btn_8 = Button(body_frame, command=lambda: enter_values('4'), text="4", width=5, height=2, bg=color4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
btn_8.place(x=0, y=104)

btn_9 = Button(body_frame, command=lambda: enter_values('5'), text="5", width=5, height=2, bg=color4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
btn_9.place(x=59, y=104)

btn_10 = Button(body_frame, command=lambda: enter_values('6'), text="6", width=5, height=2, bg=color4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
btn_10.place(x=118, y=104)

btn_11 = Button(body_frame, command=lambda: enter_values('-'), text="-", width=5, height=2, bg=color5, fg=color2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
btn_11.place(x=177, y=104)

#Fourth Row:

btn_12 = Button(body_frame, command=lambda: enter_values('1'), text="1", width=5, height=2, bg=color4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
btn_12.place(x=0, y=156)

btn_13 = Button(body_frame, command=lambda: enter_values('2'), text="2", width=5, height=2, bg=color4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
btn_13.place(x=59, y=156)

btn_14 = Button(body_frame, command=lambda: enter_values('3'), text="3", width=5, height=2, bg=color4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
btn_14.place(x=118, y=156)

btn_15 = Button(body_frame, command=lambda: enter_values('+'), text="+", width=5, height=2, bg=color5, fg=color2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
btn_15.place(x=177, y=156)

#Fifth Row:

btn_16 = Button(body_frame, command=lambda: enter_values('0'), text="0", width=11, height=2, bg=color4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
btn_16.place(x=0, y=208)

btn_17 = Button(body_frame, command=lambda: enter_values('.'), text=".", width=5, height=2, bg=color4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
btn_17.place(x=118, y=208)

btn_18 = Button(body_frame, command=calculate, text="=", width=5, height=2, bg=color5, fg=color2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
btn_18.place(x=177, y=208)

#Creating function:

window.mainloop()
