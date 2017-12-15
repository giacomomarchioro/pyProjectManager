# -*- coding: utf-8 -*-
"""
Created on Fri Aug 05 16:19:01 2016

@author: Giacomo Marchioro 2017
"""
import cPickle 
import time 
from  datetime import datetime
import os

class ProjectManager:
    
    def __init__(self):
        self.projects = {}
        self.workingon = None
        self.watching_folders = ["C:\Users\OPdaTe\Pictures","C:\Users\OPdaTe\Videos"]
        self.path = r'C:\Users\OPdaTe\Documents'
        
    def inizialize(self):
        path = os.path.join(self.path,'pyProjectManagement')
        if not os.path.exists(path):
            os.makedirs(path)
            
        with open(os.path.join(path,'log.txt'),'wb') as f:
            f.write('created Project Management')


    
    def newproject(self,name):
        if name not in self.projects.keys():
            self.projects[name] = Project(name)
        else:
            print "Project already exist!"
    
    def __append(self,info):
        '''
        This method is used to append to the daily logfile
        '''
        today = datetime.now()
        name  ='%s_%s_%s.txt' %(today.day, today.month, today.year)
        with open(os.path.join(self.path,"pyProjectManagement",name),'a') as f:
            f.write(r'%s:%s:%s -> %s' %(today.hour,today.minute,today.second,info)+ '\n')
    
    def go_to_break(self):
        self.__append('BREAK')
    
    def go_to_lunch(self):
        self.__append('LUNCH')
    
    def go_to_meeting(self):
        self.__append('MEETING')
    
    def take_note(self,note):
        self.__append('!%s' %(note))
    
    def workon(self,project):
        pro = self.projects[project]
        self.__append(pro.name)
        self.workingon = pro
        
    def _end(self):
        self.__append('END')
    
    def save(self):
        cPickle.dump()
        
    def create_daily_update(self):
        today = datetime.now()
        timestamp = time.time() #seems faster is a float 
        import os.path, time
        name  ='%s_%s_%s.txt' %(today.day, today.month, today.year)
        ranges = {}
        tmp_range = []
        with open(os.path.join(self.path,"pyProjectManagement",name),'r') as f:
            print f.read()
            
        for i in self.watching_folders:
            listdir = os.listdir(i)
            
            for j in listdir:
                path = os.path.join(i,j)
                print "last modified: %s" % time.ctime(os.path.getmtime(path))
                print "created: %s" % time.ctime(os.path.getctime(path))
        


class Project:
    
    def __init__(self,name):
        self.name=name
        self.subprojects=[]
        self.tasks = []
        self.start=None
        self.finsh=None
        self.status='Active'
        self.cost = None
        self.skills = None
    
    def test(self):
        pass

class Task:
    def __init__(self,name):
        self.name = name
        self.status = None
        self.cost = None
        self.skills = None
        self.start=None
        self.finsh=None
        self.status='Active'
    
    def test():
        pass
        
a = ProjectManager() 
        
