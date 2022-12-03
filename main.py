from tkinter import *
from func import file_catcher, return_path, Image_frame, watermark_menu


def update():
    global canvas
    if return_path() is not None:
        data = return_path()
        canvas = Image_frame(gui, data)
        canvas.grid(column=0, row=0)


gui = Tk()

gui.title('Watermarking Tool')

gui.geometry("1200x547")

gui.resizable(False, False)

menubar = Menu(gui)
menubar.add_cascade(label="Select files", underline=0, command=file_catcher)
menubar.add_cascade(label="Upload", underline=0, command=update)

canvas = Image_frame(gui)
canvas.grid(column=0, row=0)

menu = watermark_menu(gui)
menu.grid(column=1, row=0, sticky="N")

gui.config(menu=menubar)

gui.wm_attributes('-toolwindow', True)


gui.mainloop()
