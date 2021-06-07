# Python 3.9
# File name: google_earth_driver.py
# Description: start and drive Google Earth to visit locations and download images
# Authors: Aaron Watt
# Date: 2021-06-06

# Standard library imports
from pywinauto.application import Application
from pywinauto.base_wrapper import ElementNotVisible
import pywinauto.mouse as mouse
import pywinauto.keyboard as keyboard
from pathlib import Path
import os
import re
import win32api
from time import sleep

# Third-party imports

# Local application imports


# FUNCTIONS --------------------------
def connect_ge():
    app = Application().connect(title_re=".*Google Earth Pro.*")
    return app

def start_ge():
    """Start Google Earth Engine, return running application"""
    ## Find the path to the Google Earth Pro executable
    ge_path = find_ge()
    ## Search for googleearth.exe
    ## Use str() on Path because Application.start parses the string
    app = Application().start(str(ge_path))
    return app

def find_ge():
    """Search computer for googleearth.exe, return pathlib Path

    Must escape the "." in the regular expression using the "\" so it will only return
    ".exe" and not other "_exe" files.
    """
    p = find_file_in_all_drives("googleearth\.exe")
    return Path(p)

def find_file(root_folder, rex):
    """Search all folders from root_folder for our regex file pattern, return path of file"""
    for root,dirs,files in os.walk(root_folder):
        for f in files:
            result = rex.search(f)
            if result:
                return Path(os.path.join(root, f))
    ## Return None if we can't find the file in this root_folder
    return None

def find_file_in_all_drives(file_name):
    """Search for the file in all drives on this computer."""
    ## Create a regular expression for the file
    rex = re.compile(file_name)
    for drive in win32api.GetLogicalDriveStrings().split('\000')[:-1]:
        path = find_file( drive, rex )
        if path:
            ## If we found the file, return the path
            return path


def get_window():
    """Return window to interact with"""
    # Start Google Earth application
    app = start_ge()
    # Sleep while the application opens
    sleep(2)
    # Get main window
    window = app.window(title_re=".*Google Earth Pro.*")

def print_children(dlg, element, depth):
    """Recursively print out this element and all it's children, grandchildren, etc."""
    print('|','---|'*depth,
          element.element_info.name,
          element.element_info.handle,
          element.element_info.control_type)
    if len(element.children())>0:
        for child in element.children(visible_only=False):
            print_children(dlg, child, depth+1)


def draw_tree(dlg):
    """Prints out tree of elements for application dlg"""
    for element in dlg.children(visible_only=False):
        print_children(dlg, element, 0)

def enter_latlon(dlg, lat, lon, first=False):
    if first:
        dlg.type_keys('^f+{TAB 9} ^a %s, %s {ENTER}'%(lat, lon))
    else:
        dlg.type_keys('^f+{TAB 18} ^a %s, %s {ENTER}'%(lat, lon))



# MAIN -------------------------------
if __name__ == "__main__":
    get_window()




# REFERENCES -------------------------
"""
Starting/driving the application:
https://betterprogramming.pub/use-pywinauto-to-automate-programs-in-windows-7d4a7eb082a5

Searching for the .exe:
https://stackoverflow.com/questions/13067686/search-files-in-all-drives-using-python

pywinauto doc:
https://pywinauto.readthedocs.io/en/latest/controls_overview.html

pywinauto element methods:
    .draw_outline()
    .element_info.name
    .set_focus()
    .type_keys('')
    dlg.children()[1].children()[0].children()[1].set_focus()
    control_type='Edit', visible_only=False
    draw_tree(dlg)
    dlg.child_window(handle=1048580)



Could not find any element that is a text box (in fact, no buttons or anything)
Must have been hidden in some way by the developers
    search_box = dlg.child_window(title='', control_type="Edit", visible_only=False)
    search = dlg.child_window(title_re="search",
                                    depth=3)  # search only for 1 level below
                                    
    dlg.child_window(control_type='Edit', top_level_only=False, visible_only=False).element_info.name
"""