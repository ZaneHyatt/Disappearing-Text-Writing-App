from tkinter import *
import math

BACKGROUND = "#FFFBF5"
FONT_COLOR = "#1f1f1f"
FONT_NAME = "Open Sans"

timer = None

def start_timer(event):
    global timer
    if timer:
        window.after_cancel(timer)
    count_down(10)

def count_down(count):
    count_sec = count % 60
    print(count_sec)
    if count == 10:
        T.config(foreground=FONT_COLOR)
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    if count == 9:
        T.config(foreground="#313131")
    if count == 8:
        T.config(foreground="#454545")
    if count == 7:
        T.config(foreground="#595959")
    if count == 6:
        T.config(foreground="#767676")
    if count == 5:
        T.config(foreground="#8a8a8a")
    if count == 4:
        T.config(foreground="#9d9d9d")
    if count == 3:
        T.config(foreground="#a7a7a7")
    if count == 2:
        T.config(foreground="#bbbbbb")
    if count == 1:
        T.config(foreground="#e2e2e2")
    if count == 0:
        T.delete("1.0","end")

window = Tk()
window.title("The Most Dangerous Writing App")
window.config(padx=100, pady=50, bg=BACKGROUND)

T = Text(window, height=50, width=50, wrap=WORD, font=(FONT_NAME, 32), background=BACKGROUND, fg=FONT_COLOR, highlightthickness=0)
T.configure(insertbackground='red')
T.pack()

window.bind('<Key>', start_timer)

window.mainloop()