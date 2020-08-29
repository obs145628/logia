
class DocConfig:

    def __init__(self):
        self.id = None
        self.link_in_root = False
        self.name = None
        self.time = 0
        self.type = None

    def write2file(self, path):
        with open(path, 'w') as f:
            f.write('id = {}\n'.format(self.id))
            f.write('link-in-root = {}\n'.format("true" if self.link_in_root else "false"))
            f.write('name = {}\n'.format(self.name))
            f.write('time = {}\n'.format(self.time))
            f.write('type = {}\n'.format(self.type))
            
