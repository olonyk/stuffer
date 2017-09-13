from tkinter import IntVar, StringVar

class Quiz:
    def __init__(self, **kwargs):
        """ The constructor of a Quiz object is done either by a topic_dict which is used to build
            a set of questions or by an already defined set of questions. In either case a 
            DataHandler is needed.
        """
        data_handler = kwargs["data_handler"]
        if "topic_dict" in kwargs.keys():
            topic_dict = kwargs["topic_dict"]
            topic_dict = self.cast_to_bool(topic_dict)
            self.print_dict(topic_dict)
        else:
            questions = kwargs["questions"]
    
    def cast_to_bool(self, dictionary):
        """ Used to cast the topic_dict values to bool instead of IntVar.
        """
        for key, value in dictionary.items():
            if isinstance(value, dict):
                dictionary[key] = self.cast_to_bool(value)
            elif isinstance(value, IntVar):
                dictionary[key] = int(value.get())
            elif isinstance(value, StringVar):
                try:
                    dictionary[key] = int(value.get())
                except ValueError:
                    dictionary[key] = value.get()
        return dictionary

    def print_dict(self, dictionary, indentation=0):
        """ Prints the dictionary using recursive calls. This method is intended to be used while
            debugging.
        """
        for key, value in dictionary.items():
            if isinstance(value, dict):
                print("{}{}".format("\t"*indentation, key))
                self.print_dict(value, indentation=indentation + 1)
            else:
                print("{}{}\t{}".format("\t"*indentation, key, value))
