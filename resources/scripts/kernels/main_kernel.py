from tkinter import Tk, IntVar, S, N, E, W, HORIZONTAL
import tkinter as tk
from tkinter.ttk import Checkbutton, Label, Separator

from ..guis.main_gui import MainGUI
from ..support.data_handler import DataHandler
from ..support.topic_widget import TopicWidget


class MainKernel():
    def __init__(self):
        self.main_app = None
        self.data_handler = None
        self.main_root = Tk()
        self.main_app = MainGUI(self, master=self.main_root)
        self.main_root.mainloop()
    
    def populate_topics(self, gui=None):
        if not self.data_handler:
            self.data_handler = DataHandler()
        topics = self.data_handler.get_topics()
        attrib = self.data_handler.get_attrib(topics)
        if self.main_app:
            gui = self.main_app
        TopicWidget(gui.frame_topics,
                    command_1=lambda: self.toggle(gui.toggle_1, gui.values_ask),
                    command_2=lambda: self.toggle(gui.toggle_2, gui.values_given),
                    command_3=lambda: self.toggle(gui.toggle_3, gui.values_topics),
                    value_1=gui.toggle_1, value_2=gui.toggle_2, value_3=gui.toggle_3,
                    bkg=None).grid(row=0, sticky=W+N+E+S)
        row_count = 1
        for topic in attrib.keys():
            topic_value = IntVar()
            topic_value.set(1)
            topic_check = TopicWidget(gui.frame_topics,
                                      text=topic,
                                      value_topic=topic_value,
                                      command=self.not_implemented_yet, bkg=None)
            topic_check.grid(row=row_count,
                             sticky=W+N+E+S)
            gui.checkb_topics.append(topic_check)
            gui.values_topics.append(topic_value)
            gui.name_topics.append(topic)
            row_count += 1
            for val in attrib[topic]:
                # Ask window
                ask_value = IntVar()
                ask_value.set(1)
                given_value = IntVar()
                given_value.set(1)

                attr_check = TopicWidget(gui.frame_topics, text=val, value_ask=ask_value, value_given=given_value, bkg=None)
                attr_check.grid(row=row_count, sticky=W+N+E+S)
                gui.name_subtop.append(val)
                gui.checkb_ask.append(attr_check)
                gui.values_ask.append(ask_value)
                gui.values_given.append(given_value)
                row_count += 1

    def not_implemented_yet(self):
        print("Function not implemented yet")

    def check_attr_command(self):
        print("check_attr_command")
    
    def toggle(self, value, values):
        for val in values:
            val.set(bool(value.get()))

    def launch_quiz(self):
        print("Function not implemented yet")
        quiz = Quiz(data_handler=self.data_handler, topic=(self.main_app.name_topics, self.main_app.values_topics))