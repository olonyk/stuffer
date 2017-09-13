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
        self.name_topics = []
        self.name_subtop = []

        self.toggle_1 = IntVar()
        self.toggle_2 = IntVar()
        self.toggle_3 = IntVar()
        self.toggle_1.set(1)
        self.toggle_2.set(1)
        self.toggle_3.set(1)

        # Create topics frame
        t_frame = self.build_topics_frame()
        # Create control frame
        frame_control = self.build_control_frame()
        # Layout
        t_frame.grid(row=0, column=0, sticky=S+E+W+N)
        frame_control.grid(row=0, column=1, sticky=S+N)
        # Bindings
        self.kernel.populate_topics(gui=self)
    
    def onFrameConfigure(self, event):
        """ 
        Reset the scroll region to encompass the inner frame
        """
        self.canvas_topics.configure(scrollregion=self.canvas_topics.bbox("all"))

    def build_topics_frame(self):
        """
        Building and returning the frame that will be populated with topic widgets.
        """
        # Create widgets
        t_frame = Frame(self.master, relief=GROOVE, borderwidth=2)
        lbl_topics = Label(t_frame, text="Include topics")
        self.canvas_topics = Canvas(t_frame, borderwidth=0, width=200, height=200)
        self.frame_topics = Frame(self.canvas_topics)
        self.frame_topics.grid(sticky=E+W+N+S)
        self.scroll_topics = Scrollbar(t_frame, orient="vertical", command=self.canvas_topics.yview)
        self.canvas_topics.configure(yscrollcommand=self.scroll_topics.set)
        # Layout
        lbl_topics.grid(row=0, column=0)
        self.scroll_topics.grid(row=1, column=3, sticky=E+N+S)
        self.canvas_topics.grid(row=1, column=0, columnspan=3, sticky=W+E+N+S)
        # Bindings
        self.canvas_topics.create_window((1,1), window=self.frame_topics, anchor="nw", tags="self.frame", width="100000")
        self.frame_topics.bind("<Configure>", self.onFrameConfigure)
        return t_frame

    def build_control_frame(self):
        """
        Building and returning the frame that holds the settings for the quiz.
        """
        frame_control = Frame(self.master, relief=GROOVE, borderwidth=2)
        Label(frame_control, text="Quiz settings").grid(row=0, column=0)
        Label(frame_control, text="Number of questions:").grid(row=1, column=0, sticky=W+N)
        Label(frame_control, text="Save statistics:").grid(row=2, column=0, sticky=W+N)
        self.spin_nrq = Spinbox(frame_control, from_=1, to=500, width=3)
        self.spin_nrq.grid(row=1, column=1, sticky=E)
        Checkbutton(frame_control, text="", command=self.kernel.not_implemented_yet).grid(row=2, column=1, sticky=E)
        Button(frame_control, text="Start quiz", command=self.kernel.launch_quiz).grid(row=10, column=1, sticky=S+E)
        return frame_control

