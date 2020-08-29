import sys

from .mdgfmdoc import MdGfmDoc

instance = None

def get_cmd_line():
    return ' '.join(sys.argv)

class Program:

    def __init__(self):
        global instance
        assert instance is None

        main_name = get_cmd_line()
        self.main_doc = MdGfmDoc(main_name, True)

    def instance():
        global instance
        if instance is None:
            instance = Program()
        return instance

    # Add a new document to the program output
    # Class must a child class of Document
    def add_doc(self, Class, name):
        res = Class(name, False)
        self.on_add(res)
        return res

    def on_add(self, doc):
        self.main_doc.write("- ")
        self.main_doc.doc_link(doc)
        self.main_doc.write("\n")
        self.main_doc.flush()
    
