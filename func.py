from tkinter import *
from PIL import Image, ImageTk, ImageDraw, ImageFont
from tkinter import filedialog, Frame
from tkinter import ttk
import obj_dragg_able as drag


class Image_frame(Frame):
    def __init__(self, master, data=None, cwidth=900, cheight=535):
        Frame.__init__(self, master, relief=RAISED)
        self.canvasWidth = cwidth
        self.canvasHeight = cheight
        self.canvas = Canvas(self, width=self.canvasWidth, height=self.canvasHeight, highlightthickness=1,
                             highlightbackground="black")
        if data is not None:
            self.canvas.grid_forget()
            self.new_canvas = Canvas(self, width=self.canvasWidth, height=self.canvasHeight, highlightthickness=1,
                                     highlightbackground="black")
            self.image = Image.open(data[0])
            self.picture = ImageTk.PhotoImage(self.image)
            self.new_canvas.create_image(cwidth / 2, cheight / 2, image=self.picture)
            if len(data) > 1:
                self.new_canvas.create_text(800, 450, text=f"and {len(data) - 1} More", font=("bold", 22))
            self.new_canvas.grid(row=0, column=0, padx=5, pady=5)
        else:
            self.canvas.grid(row=0, column=0, padx=5, pady=5)


class watermark_menu(Frame):
    text_frame: Frame

    def __init__(self, master):
        Frame.__init__(self, master)
        self.img_w_text = None
        self.frame = None
        self.logo_paths = None
        self.separator_0 = ttk.Separator(self, orient='vertical')
        self.menu_label = Label(self, text="Menu")
        self.selected_option = StringVar(self)
        self.text_label = Label(self, text="Text :")
        self.text = Entry(self)

        self.text_opt = ["normal", "bold", "roman", "italic", "underline", "overstrike"]
        self.var = StringVar(self)
        self.var.set(self.text_opt[0])
        self.text_suggest = OptionMenu(self, self.var, *self.text_opt, command=self.insert_font)

        self.color_label = Label(self, text="Color :")
        self.color = Entry(self)
        self.color.delete(0, END)
        self.color.insert(0, "black")
        self.color_opt = ["black", "green", "yellow", "red", "pink", 'violet']
        self.col_var = StringVar(self)
        self.col_var.set(self.color_opt[0])
        self.color_suggest = OptionMenu(self, self.col_var, *self.color_opt, command=self.insert_color)

        self.style_label = Label(self, text="Font :")
        self.style = Entry(self)
        self.style.delete(0, END)
        self.style.insert(0, "normal")
        self.text_size_label = Label(self, text="Size :")
        self.text_size = Entry(self)
        self.text_size.delete(0, END)
        self.text_size.insert(0, 20)
        self.size_opt = [20, 25, 30, 40, 45, 50]
        self.siz_var = StringVar(self)
        self.siz_var.set(self.size_opt[0])
        self.size_suggest = OptionMenu(self, self.siz_var, *self.size_opt, command=self.insert_size)

        self.text_insert = Button(self, text="Insert Text", command=self.insert_text)

        self.separate = ttk.Separator(self, orient='horizontal')

        self.logo_label = Label(self, text="Select :")
        self.logo = Button(self, text="Logo", command=self.select_logo)

        self.logo_insert = Button(self, text="Insert Logo", command=self.insert_logo)

        self.separate_2 = ttk.Separator(self, orient='horizontal')

        self.apply = Button(self, text="Apply to all", command=self.apply_watermark)

        self.separator_0.grid(column=0, row=0, rowspan=15, sticky="NS")

        self.menu_label.grid(row=0, column=1, pady=10, sticky="N")
        self.text_label.grid(row=1, column=1, pady=3, sticky="e")
        self.text.grid(row=1, column=2, pady=3)

        self.color_label.grid(row=2, column=1, pady=3, sticky="e")
        self.color.grid(row=2, column=2, pady=3)
        self.color_suggest.grid(row=2, column=3, sticky="w")

        self.style_label.grid(row=3, column=1, pady=3, sticky="e")
        self.style.grid(row=3, column=2, pady=3)
        self.text_suggest.grid(row=3, column=3, pady=3)

        self.text_size_label.grid(row=4, column=1, pady=3, sticky="e")
        self.text_size.grid(row=4, column=2, pady=3)
        self.size_suggest.grid(row=4, column=3, pady=3, sticky="w")
        self.text_insert.grid(row=5, column=2, pady=10, sticky="e")

        self.separate.grid(row=6, column=1, columnspan=10, pady=10, sticky="ew")

        self.logo_label.grid(row=7, column=1, sticky="e")
        self.logo.grid(row=7, column=2, sticky="ws")

        self.logo_insert.grid(row=8, column=2, pady=20, sticky="e")

        self.separate_2.grid(row=9, column=1, columnspan=10, pady=10, sticky="ew")

        self.apply.grid(row=10, column=2, pady=80, sticky="e")

    def apply_watermark(self):
        text_cord = drag.data_text
        logo_cord = drag.data_logo
        if return_path() is not None:
            save_dir = filedialog.askdirectory(title="Choose a Folder")
            for char in return_path():

                with Image.open(char) as img:
                    w, h = img.size
                # print(905 / 2 - int(h) / 2)
                # print(f"w: {w} h: {h}")
                # print(text_cord)
                # print(905 / 2 + int(h) / 2)

                    if logo_cord is not None:
                        if 907 / 2 + int(h) / 2 > int(text_cord["x"]) > 905 / 2 - int(h) / 2:
                            if 537 / 2 + int(w) / 2 > int(text_cord["y"]) > 535 / 2 - int(w) / 2:
                                st_x = int(text_cord["x"]) - int(h)
                                x = int(text_cord["x"]) - st_x
                                st_y = int(text_cord["y"]) - int(w)
                                y = int(text_cord["y"]) - st_y
                                image_copy = img.copy()
                                image_logo = Image.open(self.logo_paths)
                                logo_copy = image_logo.copy()
                                image_copy.paste(logo_copy, (x, y))
                                image_copy.save(char)

                    with Image.open(char) as img_:
                        w, h = img_.size
                    if text_cord is not None:
                        if 907 / 2 + int(h) / 2 > int(text_cord["x"]) > 905 / 2 - int(h) / 2:
                            if 537 / 2 + int(w) / 2 > int(text_cord["y"]) > 535 / 2 - int(w) / 2:
                                st_x = int(text_cord["x"]) - int(h)
                                x = int(text_cord["x"]) - st_x
                                st_y = int(text_cord["y"]) - int(w)
                                y = int(text_cord["y"]) - st_y
                                pilled_img = ImageDraw.Draw(img_)
                                my_font = ImageFont.truetype(f"{self.style.get()}.ttf", int(self.text_size.get()), index=0, encoding='', layout_engine=None)
                                pilled_img.text((x, y), text=self.text.get(), font=my_font, fill=self.color.get())
                                img_.save(char)

    def insert_text(self):
        if return_path() is not None:
            if self.text.get() != '' and self.style.get() != '' and self.text_size.get() != '':
                if (self.text_size.get()).isnumeric():
                    if (self.style.get()).isascii():
                        if self.text_insert["text"] == "Insert Text":
                            self.text_frame = Frame(height=64, width=64, bg="white", highlightthickness=0)
                            self.text_frame.text = Label(self.text_frame, text=self.text.get(),
                                                         font=(self.style.get(), self.text_size.get()),
                                                         fg=self.color.get(), highlightthickness=0)
                            self.text_frame.text.pack()
                            drag.make_draggable_component(self.text_frame.text)
                            drag.make_draggable(self.text_frame)
                            self.text_frame.place(x=10, y=10)
                            self.text_insert["text"] = "Delete text"
                        elif self.text_insert["text"] == "Delete text":
                            self.text_frame.destroy()
                            drag.del_cords("text")
                            self.text_insert["text"] = "Insert Text"

    def insert_logo(self):
        if return_path() is not None:
            if self.logo_paths is not None:
                if self.logo_insert["text"] == "Insert Logo":
                    image = Image.open(self.logo_paths)
                    resized = image.resize((50, 50))
                    w, h = resized.size
                    self.frame = Frame(height=h, width=w, bd=0, bg="white", highlightthickness=0)
                    self.frame.picture = ImageTk.PhotoImage(resized)
                    self.frame.canvas = Canvas(self.frame, bg='white', highlightthickness=0, width=w, height=h)
                    self.frame.canvas.create_image(w / 2, h / 2, image=self.frame.picture)
                    self.frame.canvas.pack()
                    drag.make_draggable_component(self.frame.canvas)
                    drag.make_draggable(self.frame)
                    self.frame.place(x=50, y=50)
                    self.logo_insert["text"] = "Delete Logo"
                elif self.logo_insert["text"] == "Delete Logo":
                    self.frame.destroy()
                    drag.del_cords("logo")
                    self.logo_insert["text"] = "Insert Logo"

    def select_logo(self):
        data = filedialog.askopenfilename(title="Choose a Logo",
                                          filetypes=[('image files', ('.png', '.jpg'))])
        if data != '':
            self.logo_paths = data

    def insert_color(self, color):
        self.color.delete(0, END)
        self.color.insert(0, color)

    def insert_font(self, font):
        self.style.delete(0, END)
        self.style.insert(0, font)

    def insert_size(self, size):
        self.text_size.delete(0, END)
        self.text_size.insert(0, size)


img_paths = None


def return_path():
    if img_paths is not None:
        if len(img_paths) > 0:
            return img_paths
        else:
            return None


def file_catcher():
    global img_paths
    img_paths = filedialog.askopenfilenames(title="Choose Images", filetypes=[('image files', ('.png', '.jpg'))], )
