from tkinter.ttk import Frame, Radiobutton, Label, Scrollbar, Button, OptionMenu, Entry
from tkinter import Spinbox, IntVar
from tkinter import *

class MainGUI(Frame):
    def __init__(self, kernel, master=None):
        self.master = master
        self.master.title("Stuffer 2000")
        Frame.__init__(self, master)
        self.kernel = kernel

        # Create the list of checkboxes and their values
        self.checkb_topics = []
        self.checkb_ask = []
        self.checkb_given = []
        self.values_topics = []
        self.values_ask = []
        self.values_given = []

        self.toggle_1 = IntVar()
        self.toggle_2 = IntVar()
        self.toggle_3 = IntVar()
        self.toggle_1.set(1)
        self.toggle_2.set(1)
        self.toggle_3.set(1)

        # Create topics frame
        t_frame = self.build_topics_frame()
        # Create ask frame

        # Create the top labels
        
        lbl_ask = Label(self.master, text="Ask about:")
        lbl_given = Label(self.master, text="Given information:")

        

        # Create control frame
        frame_control = self.build_control_frame()

        # Layout
        # -Row 0
        t_frame.grid(row=0, column=0, sticky=W+N)
        frame_control.grid(row=0, column=3, rowspan=3, sticky=W+N)

        # -Row 2
        

        # Bindings
        self.kernel.populate_topics(gui=self)
        #self.kernel.populate_attrib(gui=self)
    
    def onFrameConfigure(self, event):
        '''Reset the scroll region to encompass the inner frame'''
        self.canvas_topics.configure(scrollregion=self.canvas_topics.bbox("all"))
    
    def toggle(self, values, func, btn):
        if len(values) > 0:
            new_setting = not bool(values[0].get())
        for item in values:
            item.set(int(new_setting))
        if new_setting:
            btn["text"] = "-"
        else:
            btn["text"] = "+"
        #func()

    def build_topics_frame(self):
        # Create widgets
        t_frame = Frame(self.master, relief=GROOVE, borderwidth=2)
        lbl_topics = Label(t_frame, text="Topics:")
        self.canvas_topics = Canvas(t_frame, borderwidth=0, background="white", width=200, height=200)
        self.frame_topics = Frame(self.canvas_topics, background="white")
        self.frame_topics.grid(sticky=E+W+N+S)
        self.scroll_topics = Scrollbar(t_frame, orient="vertical", command=self.canvas_topics.yview)
        self.canvas_topics.configure(yscrollcommand=self.scroll_topics.set)
        self.toggle_topics = Button(t_frame, text="-", command=lambda:self.toggle(self.values_topics, self.kernel.check_topic_command, self.toggle_topics))
        self.toggle_ask = Button(t_frame, text="-", command=lambda:self.toggle(self.values_ask, self.kernel.check_attr_command, self.toggle_ask))
        self.toggle_given = Button(t_frame, text="-", command=lambda:self.toggle(self.values_given, self.kernel.check_attr_command, self.toggle_given))

        # Layout
        lbl_topics.grid(row=0, column=0, sticky=W+N)
        self.scroll_topics.grid(row=1, column=3, sticky=E+N+S)
        self.canvas_topics.grid(row=1, column=0, columnspan=3, sticky=W+E+N+S)
        self.toggle_topics.grid(row=2, column=0)
        self.toggle_ask.grid(row=2, column=1)
        self.toggle_given.grid(row=2, column=2)

        # Bindings
        self.canvas_topics.create_window((1,1), window=self.frame_topics, anchor="nw", tags="self.frame", width="100000")
        self.frame_topics.bind("<Configure>", self.onFrameConfigure)

        return t_frame



    def build_control_frame(self):
        frame_control = Frame(self.master, relief=GROOVE, borderwidth=2)
        lbl_nrq = Label(frame_control, text="Number of questions:")
        self.spin_nrq = Spinbox(frame_control, from_=1, to=500)

        lbl_nrq.grid(row=0, column=0, sticky=W+N)
        self.spin_nrq.grid(row=0, column=1, sticky=W+N)
        return frame_control
