# This code is an example for a tutorial on Ubuntu Unity/Gnome AppIndicators:
# http://candidtim.github.io/appindicator/2014/09/13/ubuntu-appindicator-step-by-step.html

import os
import signal
import json



from gi.repository import Gtk as gtk
from gi.repository import AppIndicator3 as appindicator
from gi.repository import Notify as notify


APPINDICATOR_ID = 'myappindicator'
projects = {'Scan4Reco': ['do-this', 'write-this'],'SUPSI':['task2','task3']}

def main():
    indicator = appindicator.Indicator.new(APPINDICATOR_ID, 
                                           os.path.abspath('sample_icon.svg'), 
                                           appindicator.IndicatorCategory.SYSTEM_SERVICES)
    indicator.set_status(appindicator.IndicatorStatus.ACTIVE)
    indicator.set_menu(build_menu())
    notify.init(APPINDICATOR_ID)
    gtk.main()

def build_menu():

    menu = gtk.Menu()
    menu_browser = gtk.MenuItem('Launch browser')
    menu.append(menu_browser)
    # Common actions 
    separator_act = gtk.SeparatorMenuItem()
    menu.append(separator_act)
    #Menu Go to
    menu_goto = gtk.MenuItem('Go to ...')
    menu.append(menu_goto)
    #Sub menu 
    submenu_goto = gtk.Menu()
    menu_goto.set_submenu(submenu_goto) 
    # Add a fixed entry Lunch
    submenugoto_item_0 = gtk.MenuItem("Lunch")
    submenu_goto.append(submenugoto_item_0)
    # Add a fixed entry Break
    submenugoto_item_1 = gtk.MenuItem("Break")
    submenu_goto.append(submenugoto_item_1)
    # Add a fixed entry Meeting
    submenugoto_item_2 = gtk.MenuItem("Meeting")
    submenu_goto.append(submenugoto_item_2)
    # add separetor
    separator = gtk.SeparatorMenuItem('Projects')
    menu.append(separator)
    # This should be repeated for every active project
    for i in projects:
        menu_item = gtk.MenuItem(i)
        menu.append(menu_item)

        #Sub menu
        submenu = gtk.Menu()
        menu_item.set_submenu(submenu)
        # Add a fixed entry
        submenu_item_0 = gtk.MenuItem("Add task")
        submenu.append(submenu_item_0)
        separator = gtk.SeparatorMenuItem()
        # Add separator
        submenu.append(separator)
        # Dynamic options
        for task in projects[i]:
            submenu_item = gtk.MenuItem(task)
            submenu.append(submenu_item)
    
    # REPORT
    separator_rep = gtk.SeparatorMenuItem()
    menu.append(separator_rep)
    menu_rep = gtk.MenuItem('Report')
    menu_rep.connect('activate', quit)
    menu.append(menu_rep)
    # QUIT
    separator = gtk.SeparatorMenuItem()
    menu.append(separator)
    menu_quit = gtk.MenuItem('Quit')
    menu_quit.connect('activate', quit)
    menu.append(menu_quit)
    menu.show_all()


    return menu




def quit(_):
    notify.uninit()
    gtk.main_quit()

if __name__ == "__main__":
    signal.signal(signal.SIGINT, signal.SIG_DFL)
    main()
