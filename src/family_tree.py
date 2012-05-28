'''
Created on May 9, 2012

@author: MUNEER
'''
class Person(object):
    def __init__(self, name, sex):
        self.name = name
        self.sex = sex
        self.__father, self.__mother = None, None
        self.children = []
        self.spouse = None
    
    def get_father(self):
        return self.__father
    
    def set_father(self,person):
        try:
            if person.sex=='male' and person not in self.children \
                and person not in self.spouse:
                self.__mother = person
        except:
            pass
            
    
    def get_mother(self):
        return self.__mother
    
    def set_mother(self,person):
        try:
            if person.sex=='female' and person not in self.children \
                and person not in self.spouse:
                self.__mother = person
        except:
            pass
    
    def get_parents(self):
        return (self.__father, self.__mother)
    
    def get_wife(self):
        return self.spouse if self.sex=='male' else None
    
    def get_husband(self):
        return self.spouse if self.sex=='female' else None
    
    def get_brothers(self):
        if self.__father:
            paternal_brothers = [child for child in self.__father.children
                                 if child.sex=='male']
        if self.__mother:
            maternal_brothers = [child for child in self.__mother.children
                                 if child.sex=='male']
        total_brothers = list(set(paternal_brothers+maternal_brothers))
        if self in total_brothers:
            total_brothers.remove(self)
        return total_brothers
    
    def get_sisters(self):
        if self.__father:
            paternal_sisters = [child for child in self.__father.children
                                 if child.sex=='female']
        if self.__mother:
            maternal_sisters = [child for child in self.__mother.children
                                 if child.sex=='female']
        total_sisters = list(set(paternal_sisters+maternal_sisters))
        if self in total_sisters:
            total_sisters.remove(self)
        return total_sisters
    def get_children(self):
        return self.children
    
    