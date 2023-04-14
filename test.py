import tkinter as tk
import tkinter.ttk as ttk
from ctypes import windll


class TestApp(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)

        # set overrideredirect to True to remove the windows default decorators
        self.overrideredirect(True)

        self.geometry('700x500+10+10')  # you may or may not want to initialize the geometry of the window
        self.minsize(193, 109)

        # (x, y) coordinates from top left corner of the window
        self.x = None
        self.y = None

        # Create a frame that will contain the title label of the window
        self.frame = tk.Frame(self, bg='gray38')
        self.frame.pack(side=tk.TOP, fill=tk.X)

        # Label `name` for the window
        # Since buttons are on the right side and the name of the window is on the left side, the label will be packed towards LEFT side
        self.name = tk.Label(self.frame, text='Simple Text Box', font='Consolas 11',
                             bg=self.frame.cget('background'), fg='white')
        self.name.pack(side=tk.LEFT, fill=tk.X, anchor=tk.CENTER)

        # Pack the close button to the right-most side
        self.close = tk.Button(self.frame, text='✕', bd=0, width=3, font='Consolas 13',
                               command=self.destroy, bg=self.frame.cget('background'))
        self.close.pack(side=tk.RIGHT)

        # Pack the maximize button second from the right
        # The unicode string as the value of the keyword `text` below, is taken from the internet, it contains the maximize icon as unicode character
        self.maximize = tk.Button(self.frame, text=u"\U0001F5D6", bd=0, width=3, font='Consolas',
                                  command=self.maximize_win, bg=self.frame.cget('background'))
        self.maximize.pack(side=tk.RIGHT)

        # Pack the minimize button third from the right
        self.minimize = tk.Button(self.frame, text='—', bd=0, width=3, font='Consolas 13',
                                  command=self.minimize_win, bg=self.frame.cget('background'))
        self.minimize.pack(side=tk.RIGHT)

        # -------------------
        # NOW YOU CAN PUT WHATEVER WIDGETS YOU WANT AFTER THIS BUT FOR THIS EXAMPLE I
        # HAVE TAKEN A TEXTBOX WITH HORIZONTAL AND VERTICAL SCROLLBARS AND A SIZEGRIP
        # -------------------

        # The frame below contains the vertical scrollbar and the sizegrip (sizegrip helps in resizing the window
        self.scroll_frame = tk.Frame(self)
        v_scroll = tk.Scrollbar(self.scroll_frame, orient=tk.VERTICAL)
        h_scroll = tk.Scrollbar(self, orient=tk.HORIZONTAL)
        self.grip = ttk.Sizegrip(self.scroll_frame)

        # I am directly putting the textbox in the window, you may add frames and other stuff
        self.text = tk.Text(self, wrap=tk.NONE, yscrollcommand=v_scroll.set, xscrollcommand=h_scroll.set,
                            font='Consolas 14', width=1, height=1)

        # set the scrollbar for y and x views of the textbox respectively
        v_scroll.config(command=self.text.yview)
        h_scroll.config(command=self.text.xview)

        # Packing scrollbar frame, the scrollbars and the grip according to the arrangement I want
        self.scroll_frame.pack(side=tk.RIGHT, fill=tk.Y)
        v_scroll.pack(side=tk.TOP, fill=tk.Y, expand=tk.Y)
        self.grip.pack(side=tk.BOTTOM)
        self.text.pack(side=tk.TOP, expand=tk.TRUE, fill=tk.BOTH)
        h_scroll.pack(side=tk.BOTTOM, fill=tk.X)
        
        self.grip.bind("<B1-Motion>", self.onmotion)
        # Bind the motion of mouse after mouse click to the onmotion function for window resizing

        self.call('encoding', 'system', 'utf-8')

        # Binding `<Enter>` and `<Leave>` mouse event to their respective functions
        # `<Enter>` event is called when the mouse pointer enters any widget
        # `<Leave>` event is called when the mouse pointer leaves any widget
        # Here when the mouse pointer enters or leaves the buttons their color will change
        self.close.bind('<Enter>', lambda _: self.close.config(bg='red'))
        self.close.bind('<Leave>', lambda _: self.close.config(bg=self.frame.cget('background')))
        self.minimize.bind('<Enter>', lambda _: self.minimize.config(bg='gray58'))
        self.minimize.bind('<Leave>', lambda _: self.minimize.config(bg=self.frame.cget('background')))
        self.maximize.bind('<Enter>', lambda _: self.maximize.config(bg='gray58'))
        self.maximize.bind('<Leave>', lambda _: self.maximize.config(bg=self.frame.cget('background')))

        # Now you may want to move your window (obviously), so the respective events are bound to the functions
        self.frame.bind("<ButtonPress-1>", self.start_move)
        self.frame.bind("<ButtonRelease-1>", self.stop_move)
        self.frame.bind("<B1-Motion>", self.do_move)
        self.frame.bind('<Double-1>', self.maximize_win)
        self.name.bind("<ButtonPress-1>", self.start_move)
        self.name.bind("<ButtonRelease-1>", self.stop_move)
        self.name.bind("<B1-Motion>", self.do_move)
        self.name.bind('<Double-1>', self.maximize_win)

    def start_move(self, event):
        """ change the (x, y) coordinate on mousebutton press and hold motion """
        self.x = event.x
        self.y = event.y

    def stop_move(self, event):
        """ when mouse button is released set the (x, y) coordinates to None """
        self.x = None
        self.y = None

    def do_move(self, event):
        """ function to move the window """
        self.wm_state('normal')  # if window is maximized, set it to normal (or resizable)
        self.maximize.config(text=u"\U0001F5D6")  # set the maximize button text to the square character of maximizing window
        deltax = event.x - self.x
        deltay = event.y - self.y
        x = self.winfo_x() + deltax
        y = self.winfo_y() + deltay
        self.geometry(f"+{x}+{y}")

    def onmotion(self, event):
        """ function to change window size """
        self.wm_state('normal')
        self.maximize.config(text=u"\U0001F5D6")
        x1 = self.winfo_pointerx()
        y1 = self.winfo_pointery()
        x0 = self.winfo_rootx()
        y0 = self.winfo_rooty()
        self.geometry("%sx%s" % ((x1-x0), (y1-y0)))
        return

    def minimize_win(self, event=None):
        """ function to iconify or minimize window as an icon """
        self.overrideredirect(False)
        self.wm_iconify()
        self.bind('<FocusIn>', self.on_deiconify)

    def maximize_win(self, event=None):
        """ function to maximize window or make it normal (exit maximize) """
        if self.maximize.cget('text') == u"\U0001F5D7":
            self.wm_state('normal')
            self.maximize.config(text=u"\U0001F5D6")
            return
        self.wm_state('zoomed')
        self.maximize.config(text=u"\U0001F5D7")

    def on_deiconify(self, event):
        """ function to deiconify or window """
        self.overrideredirect(True)
        set_appwindow(root=self)


def set_appwindow(root):
    hwnd = windll.user32.GetParent(root.winfo_id())
    style = windll.user32.GetWindowLongPtrW(hwnd, GWL_EXSTYLE)
    style = style & ~WS_EX_TOOLWINDOW
    style = style | WS_EX_APPWINDOW
    res = windll.user32.SetWindowLongPtrW(hwnd, GWL_EXSTYLE, style)
    # re-assert the new window style
    root.wm_withdraw()
    root.after(10, lambda: root.wm_deiconify())


if __name__ == '__main__':
    GWL_EXSTYLE = -20
    WS_EX_APPWINDOW = 0x00040000
    WS_EX_TOOLWINDOW = 0x00000080

    app = TestApp()
    # print(app.tk.call('tk', 'windowingsystem'))
    # # Here root.tk.call('tk', 'windowingsystem') calls tk windowingsystem in Tcl, and that returns 'win32',
    # # 'aqua' or 'x11' as documented in tk
    app.after(10, lambda: set_appwindow(root=app))
    app.text.insert(1.0, 'Drag the window using the title or the empty area to the right of the\ntitle.'
                         ' Try maximizing / minimizing.\n\n-- YOU MAY HAVE A PROBLEM WITH RESIZING --\n'
                         '-- ALSO IF YOU REMOVE `height` AND `width` KEYWORDS FROM THE TEXTBOX DECLARATION'
                         ' AND FONT SIZE IS TOO BIG THE SCROLLBAR MAY DISAPPEAR --\nSO KEEP THOSE KEYWORDS THERE!')
    app.mainloop()
    