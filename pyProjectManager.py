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
        self.watching_folders = [r"/home/opdate/Pictures",r'/home/opdate/Documents/Litterature']
        self.path = r'/home/opdate/'
        
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
        import os.path, time
        today = datetime.now()
        timestamp = time.time() #seems faster is a float 
        
        name  ='%s_%s_%s.txt' %(today.day, today.month, today.year)
        ranges = {}
        tmp_range = []
        files  = {}
        with open(os.path.join(self.path,"pyProjectManagement",name),'r') as f:
            time, tags = f.read().split('->')
            ranges[time] = tags
            
        for wfolder in self.watching_folders:
            listdir = os.listdir(wfolder)
            
            for wfile in listdir:
                path = os.path.join(wfolder,wfile)
                ct = time.ctime(os.path.getmtime(path))
                mt = time.ctime(os.path.getctime(path))
                if ct:
                    print 'test'

class Project:
    
    def __init__(self,name):
        self.name=name
        self.working_packages_phases = []
        self.tasks = []
        self.start=None
        self.finsh=None
        self.status='Active'
        self.cost = None
        self.skills = None
        self.resources = []
    
    def test(self):
        pass

class Task:
    def __init__(self,name):
        self.name = name
        self.project = None 
        self.status = None
        self.cost = None
        self.skills = None
        self.start=None
        self.finsh=None
        self.status='Active'
        self.predecessors = []
        self.subtasks = []
        self.resources = []
        self.priority = None 
    
    def test():
        pass
        
class Resource: 
    def __init__(self,name):
        self.name = None 
        self.type = None 
        self.cost = None
        self.location = None 
        self.calendar = None 

class Deliverable:
    pass
    
    
a = ProjectManager() 
a.newproject('Scan4Reco')
a.newproject('Endoscope')
