from .document import Document

TYPE = "cmark-gfm"

class MdGfmDoc(Document):

    def __init__(self, name, link_in_root):
        super().__init__(name, TYPE, link_in_root)

    def header(self, level, title):
        self.write('{} {}\n'.format('#' * level, title))
        self.flush()
        
    def h1(self, title): self.header(1, title)
    def h2(self, title): self.header(2, title)
    def h3(self, title): self.header(3, title)
    def h4(self, title): self.header(4, title)

    def code_begin(self, lang = ""):
        self.flush()
        self.write("```{}\n".format(lang))

    def code_end(self):
        self.write("```\n")
        self.flush()

    # Insert an image (path may be local or global url)
    def img(self, label, path):
        self.write("![{}]({})\n".format(label, path))

    # Add a link to another document
    # doc_id may be the str id, or directly the document object
    def doc_link(self, doc_id, text = ""):
        if not isinstance(doc_id, str):
            if text == "":
                text = doc_id.conf.name
            doc_id = doc_id.conf.id

        self.write("[{}](#!doc-{})".format(text, doc_id))
        

    
