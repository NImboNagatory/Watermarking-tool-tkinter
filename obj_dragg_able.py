global grid
grid = 4


def save_cords(x='', y='', state=''):
    global data_logo
    global data_text
    if x != '' and y != '':
        if state == "logo":
            data_logo = {"x": x, "y": y}
        elif state == "text":
            data_text = {"x": x, "y": y}


data_logo = None
data_text = None


def del_cords(state):
    global data_logo
    global data_text
    if state == "logo":
        data_logo = None
    elif state == "text":
        data_text = None


def make_draggable(widget):
    widget.bind("<Button-1>", on_drag_start)
    widget.bind("<B1-Motion>", on_drag_motion)
    widget.bind("<ButtonRelease-1>", on_drag_release)


def make_draggable_component(widget):
    widget.bind("<Button-1>", on_component_drag_start)
    widget.bind("<B1-Motion>", on_component_drag_motion)
    widget.bind("<ButtonRelease-1>", on_component_drag_release)


def on_drag_start(event):
    widget = event.widget
    widget._drag_start_x = event.x
    widget._drag_start_y = event.y


def on_drag_motion(event):
    widget = event.widget
    x = widget.winfo_x() - widget._drag_start_x + event.x
    y = widget.winfo_y() - widget._drag_start_y + event.y
    if 870 > x > 5 and 515 > y > 5:
        widget.place(x=x, y=y)
        if str(widget)[-6:] == "!label":
            save_cords(x, y, 'text')
        elif str(widget)[-6:] == "!canvas":
            save_cords(x, y, "logo")


def on_drag_release(event):
    global grid
    widget = event.widget
    x = round((widget.winfo_x() - widget._drag_start_x + event.x) / grid) * grid
    y = round((widget.winfo_y() - widget._drag_start_y + event.y) / grid) * grid
    if 870 > x > 5 and 515 > y > 5:
        widget.place(x=x, y=y)
        if str(widget)[-6:] == "!label":
            save_cords(x, y, 'text')
        elif str(widget)[-6:] == "!canvas":
            save_cords(x, y, "logo")


def on_component_drag_start(event):
    widget = event.widget
    container = widget.nametowidget(widget.winfo_parent())
    container._drag_start_x = event.x
    container._drag_start_y = event.y


def on_component_drag_motion(event):
    widget = event.widget
    container = widget.nametowidget(widget.winfo_parent())
    x = container.winfo_x() - container._drag_start_x + event.x
    y = container.winfo_y() - container._drag_start_y + event.y
    if 870 > x > 5 and 515 > y > 5:
        container.place(x=x, y=y)
        if str(widget)[-6:] == "!label":
            save_cords(x, y, 'text')
        elif str(widget)[-6:] == "!canvas":
            save_cords(x, y, "logo")


def on_component_drag_release(event):
    global grid
    widget = event.widget
    container = widget.nametowidget(widget.winfo_parent())
    x = round((container.winfo_x() - container._drag_start_x + event.x) / grid) * grid
    y = round((container.winfo_y() - container._drag_start_y + event.y) / grid) * grid
    if 870 > x > 5 and 515 > y > 5:
        container.place(x=x, y=y)
        if str(widget)[-6:] == "!label":
            save_cords(x, y, 'text')
        elif str(widget)[-6:] == "!canvas":
            save_cords(x, y, "logo")


def set_grid(measure):
    global grid
    grid = measure
