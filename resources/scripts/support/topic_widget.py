import tkinter as tk
from tkinter import HORIZONTAL, E, IntVar, N, S, Tk, W
from tkinter.ttk import (Button, Checkbutton, Entry, Frame, Label, OptionMenu,
                         Radiobutton, Scrollbar, Separator)
from tkinter import *


class TopicWidget(Frame):
    """Topic Widget is a collection of checkbuttons and labels to be put in a tree like
       structure."""
    def __init__(self, master=None, **kwargs):
#text=None, value_topic=None, value_ask=None, value_given=None,
 #                command=None, bkg=None):
        """Constructor of the topic widget"""
        Frame.__init__(self, master)
        self.configure(background=kwargs["bkg"])
        self.master = master

        if "value_topic" in kwargs.keys():
            self.build_topic(kwargs["text"], kwargs["value_topic"], kwargs["command"], kwargs["bkg"])
        elif "value_ask" in kwargs.keys():
            self.build_attribute(kwargs["text"], kwargs["value_ask"], kwargs["value_given"], kwargs["bkg"])
        else:
            self.build_head(kwargs)

    def build_topic(self, text, value_topic, command, bkg):
        """Creates a topic widget, i.e. a main node of a tree"""
        self.grid_columnconfigure(1, weight=1)
        Label(self, text=text, background=bkg).grid(row=0, column=0)
        Separator(self, orient=HORIZONTAL).grid(row=0, column=1, sticky=W+E)
        tk.Checkbutton(self, text="", variable=value_topic, command=command, bg=bkg,
                       highlightthickness=0, bd=0).grid(row=0, column=2)

    def build_attribute(self, text, value_ask, value_given, bkg):
        """Creates an topic widget, i.e. a leaf of a tree"""
        self.grid_columnconfigure(0, weight=1)
        self.columnconfigure(0, minsize=10)
        self.columnconfigure(1, minsize=10)
        self.columnconfigure(2, minsize=10)
        self.columnconfigure(3, minsize=15)
        Label(self, text="-{}".format(text), background=bkg).grid(row=0, column=0, sticky=W)
        tk.Checkbutton(self, text="", variable=value_ask, bg=bkg, highlightthickness=0,
                       bd=0).grid(row=0, column=1, sticky=E)
        tk.Checkbutton(self, text="", variable=value_given, bg=bkg, highlightthickness=0,
                       bd=0).grid(row=0, column=2, sticky=E)
    
    def build_head(self, options):
        """Creates a header of a tree"""
        command_1 = options["command_1"]
        value_1 = options["value_1"]
        command_2 = options["command_2"]
        value_2 = options["value_2"]
        command_3 = options["command_3"]
        value_3 = options["value_3"]
        bkg = options["bkg"]

        self.grid_columnconfigure(0, weight=1)
        self.columnconfigure(0, minsize=10)
        self.columnconfigure(1, minsize=10)
        self.columnconfigure(2, minsize=10)
        self.columnconfigure(3, minsize=15)

        tk.Checkbutton(self, text="", variable=value_1, bg=bkg, highlightthickness=0,
                       command=command_1, bd=0).grid(row=0, column=1, sticky=E)
        tk.Checkbutton(self, text="", variable=value_2, bg=bkg, highlightthickness=0,
                       command=command_2, bd=0).grid(row=0, column=2, sticky=E)
        tk.Checkbutton(self, text="", variable=value_3, bg=bkg, highlightthickness=0,
                       command=command_3, bd=0).grid(row=0, column=3, sticky=E)
