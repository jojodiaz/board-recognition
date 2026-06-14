from pathlib import Path

# Class managing the directory structure for this project. 
class DirectoryManager():
    def __init__(self,):
        pass

    def _create_structure(self, root = "."):
        root = Path(root)
        root.iterdir()
    
class Directory:
    def __init__(self, path, directories = None, files = None, permissions = None):
        self.directories = directories
        self.files = files
        self.permissions = permissions

class File:
    def __init__(self, path = None, permissions = None):
        self.path = path
        self.permissions = permissions

"""At import time, most of the directory is already structured according to
    the developers choices. However during runtime certain directories are 
    possibly created. This class allows you to 
    1. Keep track of where the aforementioned existing structure
    2. Keep track of the newly created directories
    3. Change directory paths easily.
    
    Forget this stupid shit do this later if at all the paradigm is half baked at best
    It makes no sense to have something like this unless you can define the 'important' directories 
    and there should really only be a handful and at that point this whole abstraction becomes
    useless because why not just have a config or set up the paths at the beginning, if something changes git will catch it
    unless you really fuck something up."""