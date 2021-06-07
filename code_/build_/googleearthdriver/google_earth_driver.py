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

    # TODO: select search textbox and enter locations
    # can click if we find the right place: app['Google Earth Pro']['widgetWindow'].click()
    # can print list of controls: app['Google Earth Pro'].print_control_identifiers()

    # print("Application windows:")
    # print(app.windows())
    pass



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
"""