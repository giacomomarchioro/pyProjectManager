# pyProjectManager(NOT-READY IN DEVELOPMENT).
> __One Ring to rule them all, one Ring to find them,
One Ring to bring them all and in the database bind them__

**pyProjectManager (pyPM)** is a ProjectManagment that manage itself and helps you to be more productive tracking your activity. The benefit of tracking is that it helps you avoiding loosing files, stop repeating things over and over again, integrating your workflows for reporting and publishing quickly your results. 

This simple project manger system is based on Python using a **fix-folder structure** and **auto-tagging system** that runs when you want and its dedicated file manager.

## Compared to similar things
Compared to similar things like:
  - **Zeitgeist Ubuntu** - An excellent utility for traking your activities, pyPM use minimal sys resources compared to it.
  - **[Open Science Framework](https://github.com/centerforopenscience)** - Web based for scientifc projects
  - **MyCollab,[Freedcamp](https://freedcamp.com/),[Taiga (in Python)](https://taiga.io/) etc. etc.** - Web based generic PM
  - **[Planner](https://wiki.gnome.org/action/show/Apps/Planner?action=show&redirect=Planner)** - Ubuntu app for displaying projects
  - **Odoo** - Big Python CRM with PM featuers
pyProjectManager allows you to track your activity and to use auto-tagging you don't have to update the project status pyPM will do it for you.
  - [**TaskJuggler**](http://taskjuggler.org/download.html) - Written in Ruby


# How does it works?
## Plan the project using the main app
Using the main app you can create new projects and subdivide them in tasks and subtask 
## Select the project using the system tray icon
pyPM is mainly used as a system tray icon,clicking on the icon you can select between your active projects. Once selected the project pyPM will **log** that you are working on that project and specific task and will **auto-tag** the files you are producing or modifying from now on with the project name.
## The fixed folder structure 
pyProjectManager is based on a **fixed folder structure**, **wathced folders** and **tags**. This could be a change in the way you are used to work but it really makes the difference. An example of fixed folder structure is the following:

  - Image (.jpg, .tiff, etc...)
  - Explanatory drawing  (.jpg, .tiff, etc...) 
  - Video  (.avi, .mp4, etc...)
  - Video tutorial (.avi, .mp4, etc...)
  - Script  (.py, .cpp, etc...)
  - CAD model  (.dae, .step, etc...)
  - Invoice  (.pdf, etc...)
  - Litterature (.pdf):
       - already read (.pdf)
  - Result (.jpg, .tiff, .txt etc..)
  - Presentation (.opd, .ppt, etc.)
  - Report ( .doc, .odf, etc.)
  - Instrument acquisitions (.strangeformat)
  - Projects (?)
  
The idea is when saving something to group the files sorted by **type** trying to avoid any nested folder that can be source of problems. These folders can be then add to the **watched folders list** of **PyPM** which check them regularly (e.g. when computer switch off or goes in stand-by). **PyPM** use the **log** file to assign to every file you produced the tag of the project and the task you where working on when you created it. So if you were working on the project _"Panama Canal Expansion"_ in the task _"dissemination"_ and during that time you create _escavation.avi_ file in the _Videos_ folder, the _"escavation.avi"_ file will have the following tags: .avi, Videos, Panama Canal Expansion, dissemination, yourname, path. Location name of the file and tags are stored in a database that you can access to retrive the information.

## Tag everything 
This kind of auto-tagging system allows you to tag everything that has a timestamp. You can tag browsing history (website that you visted for gethering information) emails, chats .bash_history and so on. You can transoform your screenshoot folder in a watched-folder so you can documented how you solved a task without any effort.

## Creating a deliverable 
The deliverable is something that is expected when the task is finished. You can create directly task with an **auto-updating of the status** task create [Video]. You can add further filters to it for example format specification, resolution, frame-rate specification to be respected.  

## Tagging in the file name
Some additional tags can be added in the file name the most important is `_v#` where # is a number which denotes the number of a final version. You may start creating the file "escavation.avi" with a video editor but is not ready yet this mean that the task is not compleated. When you rename it escavation_v1.avi the system will see as a final version and hence the task is marked as completed.

## Setting default save location for a software
You can change the default save location for a software depending on the project you are working at the moment. (This works for compatible software).

## Create automatically a timesheet
Often it is required to create a timesheet with the hours worked for a specific project. 

# Views
Views allow you to see you project in a graphical way, different views are available. 

## Priority view 
Tasks have a priority parameters this view allows you to rearrange the priority of a task. There is no high or low priority but a task can have a higher priority of compared to other. Tasks unclassified are consider with equal low priority.

## Gantt view 
Tipical Gantt view of the project. 
 

# Q&A:
Why is not better to create a folder for a project and store everything in it?

It depends on the size of the project but usually this have some drowbacks: the inofrmation inside can be difficult to reach again. For example imagine that you did a similar task "dissemination" where you created a nice video of your system you have to dig inside the folder structures of your project to find it. You can mix the two approaches: keep a folder for the project where you store files you are sure are not usable in others, and keep files re-usable in the fixed store structure.


Some operating systems already divides the files using their formats in video and images etc. etc. is not better to use this solution? 

It works up to a certian point when the files are not so many and you don't need specific tag. This folder structure allows you to distinguish between categories of videos (e.g. rendering, animation etc. etc.) with the same format or group different formats.
