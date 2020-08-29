import os
import random
import time

from .docconfig import DocConfig

DATA_DIR = os.path.join(os.path.dirname(__file__), "../../data")

def get_time_ms():
    return int(time.time() * 1000)

def is_legal_id_char(c):
    if c >= 'a' and c <= 'z':
        return True
    if c >= 'A' and c <= 'Z':
        return True
    if c >= '0' and c <= '9':
        return True
    return c == '_'

def gen_uid():
    UID_SIZE = 24

    res = ""
    while len(res) < UID_SIZE:
        c = chr(random.randint(0, 127))
        if is_legal_id_char(c):
            res += c

    return res
        

def build_data_dir(id):
    name = os.path.join(DATA_DIR, "doc_{}".format(id))
    os.mkdir(name)
    return name

'''
Fromatted text document
Regroups functions common to all documents types
Most of the time this class shouldn't be used directly
Instead a subclass for a specific document type should be used
'''
class Document:

    def __init__(self, name, type, link_in_root):
        self.conf = DocConfig()
        self.conf.id = gen_uid()
        self.conf.link_in_root = link_in_root
        self.conf.name = name
        self.conf.time = get_time_ms()
        self.conf.type = type

        self.dir = build_data_dir(self.conf.id)
        self.md_path = os.path.join(self.dir, "main.md")
        self.os = open(self.md_path, "w")
        self.unique = 0

        self.conf.write2file(os.path.join(self.dir, "config.txt"))

    def __del__(self):
        self.os.close()

    def name(self):
        return self.conf.name

    def id(self):
        return self.conf.id

    def doc_type(self):
        return self.conf.type

    def out_dir(self):
        return self.dir

    def write(self, data):
        if callable(getattr(data, "logia_doc_write", None)):
            data.logia_doc_write(self)
        else:
            self.os.write(data)

    def flush(self):
        self.os.flush()

    # Gen filepath of the form <out_dir>/UID<post>
    def gen_file_name(self, post = ""):
        res = "{}{}".format(self.unique, post)
        self.unique += 1
        return res

    # Gen filepath of the form <out_dir>/UID<post>
    def gen_file_path(self, post = ""):
        return os.path.join(self.dir, self.gen_file_name(post))

    # Get file path of a local file, used on the WebApp to ref this file
    def get_file_path(self, filename):
        return "/docs/doc_{}/{}".format(self.conf.id, filename)
    
