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
        self.watching_folders = [r"/home/opdate/Documents/watchfolder2/",
                                 "/home/opdate/Documents/watchfolder1/"]
        self.path = r'/home/opdate/'
        
    def inizialize(self):
        path = os.path.join(self.path,'pyProjectManagement')
        if not os.path.exists(path):
            os.makedirs(path)
        self.__append_history('created Project Management')



    
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
    
    def __append_history(self,info):
        '''
        This method is used to append to the history logfile: log.txt
        '''
        today = datetime.now()
        name  ='log.txt' 
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
        self.__append_history('Dailyupdate')
        today = datetime.now()
        #timestamp = time.time() #seems faster is a float                      
        name  ='%s_%s_%s.txt' %(today.day, today.month, today.year)
        ranges = []
        tags = []
        with open(os.path.join(self.path,"pyProjectManagement",name),'r') as f:
            for i in f:
                timex, tagsi = i.strip().split(r'->')
                hour, minutes, seconds, = timex.split(':')
                tobj = datetime(today.year, #year
                                      today.month, #month,
                                      today.day, #day
                                      int(hour),#hour
                                      int(minutes),#minutes
                                      int(seconds),#seconds
                                      )
                ranges.append(tobj) 
                tags.append(tagsi)
        ranges.append(today)
        for wfolder in self.watching_folders:
            print "*****"
            print wfolder
            print "******"
            os.chdir(wfolder)
            filenames = filter(os.path.isfile, os.listdir(wfolder))
            filespath = [os.path.join(wfolder, fi) for fi in filenames] # add path to each file
            #times_paths = dict(zip(map(os.path.getctime,filespath),filespath))
            times_paths = { os.path.getctime(i):i for i in filespath }
            #we sort the files this will speed up the search
            times_paths_sorted = sorted(times_paths.items())
            i=0
            for t,fname in times_paths_sorted:
 #               path = os.path.join(wfolder,wfile)
#                ct = time.ctime(os.path.getmtime(path))
#                mt = time.ctime(os.path.getctime(path))

                #print i

                ct = datetime.fromtimestamp(t) #time of the file

                if ct>=ranges[i] and ct < ranges[i+1]:
                    print fname, tags[i]
#                if ct> ranges[i+1]:
#                    print fname, tags[i+1]
#                    i+=1
                #we have to skip any work package where we did not create file    
                while ct > ranges[i] and ct > ranges[i+1]:
                    i+=1
                print fname, tags[i] 
        return ranges

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
