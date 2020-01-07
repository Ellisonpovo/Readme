import tkinter
window=tkinter.Tk()
window.title("GUI")
def left_click(event):
    tkinter.Label(window,text="Left click!").pack()
def middle_click(event):
    tkinter.Label(window,text="Middle click!").pack()
def right_click(event):
    tkinter.Label(window,text="Right click!").pack()

window.bind("<Button-1>",left_click)
window.bind("<Button-2>",middle_click)
window.bind("<Button-3>",right_click)
