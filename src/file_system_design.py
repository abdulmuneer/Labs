'''
design for a file system
In Progress..

Created on May 28, 2012

@author: MUNEER


Design patterns that can be applied:
COMPOSITE: for tree structure
Iterator: for traversing

'''
from datetime import datetime

class File():
    def __init__(self,name,user,group):
        self.__content = []
        self.meta = {
                     'name': name,
                     'datetime_creation' : datetime(),
                     'datetime_modification': datetime(),
                     'user': user,
                     'group': group,
                     'icon':None,
                     'size':0
                     }
    
    def read_file(self):
        pass
    
    def cut(self):
        pass
    
    def copy(self):
        pass
    
    def paste(self):
        pass
    
    def compress_file(self):
        pass
    
    def update_meta(self):
        pass
    
class Directory():
    def __init__(self,name,user,group):
        self.__files = []
        self.meta = {
                     'name': name,
                     'datetime_creation' : datetime(),
                     'datetime_modification': datetime(),
                     'user': user,
                     'group': group,
                     'icon':None,
                     'size':0
                     }
        
    def read_directory(self):
        pass
    
    def create_file(self):
        pass
    
    def cut(self):
        pass
    
    def copy(self):
        pass
    
    def paste(self):
        pass
 
    def compress_directory(self):
        pass
        
    def update_meta(self):
        pass

class Drive():
    def __init__(self,name,group):
        self.__content = []
        self.meta = {
                     'name': name,
                     'datetime_creation' : datetime(),
                     'datetime_modification': datetime(),
                     'group': group,
                     'icon':None,
                     'size':0
                     }
    def read_drive(self):
        pass
    
    def create_directory(self, name, user):
        pass
    
    def create_files(self, name, user):
        pass
    
    def compress_drive(self):
        pass
    
    def format_drive(self):
        pass
    
    def share_drive(self):
        pass
        
    def update_meta(self):
        pass
    
class FileSystem():
    def __init__(self):
        self.__drives = []
        self.meta = {}
    def add_drives(self):
        pass
    def update_meta(self):
        pass
