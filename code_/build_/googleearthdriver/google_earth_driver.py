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
from PIL import Image
from math import floor

# Third-party imports
from image_slicer import slice

# Local application imports


# FUNCTIONS --------------------------
# TODO: make into a class, using these as methods
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
    dlg = app.window(title_re=".*Google Earth Pro.*")
    sleep(1)


    data = [[44.90602112, -93.89472961],
        [44.9357, -93.802742],
        [45.579415, -122.885045],
        [43.96575165, -97.69973755]]
    first = True
    for [lat, lon] in data:
        enter_latlon(dlg, lat, lon, first=first)
        save_image()
        first = False
        sleep(1)

    print('done?')
    # Enter Search Box
    dlg.type_keys("%{DOWN}{ESC 2}{DOWN 2}^a 44.90602112, -93.89472961 {ENTER}")
    sleep(4)



    # dlg.print_control_identifiers(depth=2)
    test = dlg['main_stack_Window']
    # LeftPanelVSplitterWindow
    sleep(1)
    test.draw_outline()

    main_win_wrapper = dlg.set_focus()  # not needed if this is already in focus (needed during debug)


def print_children(dlg, element, depth):
    """Recursively print out this element and all it's children, grandchildren, etc."""
    print('|','---|'*depth,
          element.element_info.name,
          element.element_info.handle,
          element.element_info.control_type)
    if len(element.children())>0:
        for child in element.children(visible_only=False):
            print_children(dlg, child, depth+1)


def draw_tree(dlg: Application.window):
    """Prints out tree of elements for application dlg

    :param dlg:
    """
    for element in dlg.children(visible_only=False):
        print_children(dlg, element, 0)

def enter_latlon(dlg: Application.window, lat: float, lon: float, first: bool=False) -> object:
    """Types the lat-lon location into GE and executes the location change.

    :param dlg:
    :param lat:
    :param lon:
    :param first:
    """
    if first:
        dlg.type_keys('^f+{TAB 9} ^a %s, %s {ENTER}'%(lat, lon))
    else:
        dlg.type_keys('^f+{TAB 18} ^a %s, %s {ENTER}'%(lat, lon))


def change_image_resolution(pixel_width: int, pixel_length: int):
    """Change the window size to change saving image resolution to pixel_width
    by pixel_length.

    :param pixel_width: desired width of export image in pixels
    :param pixel_length: desired length of export image in pixels
    """
    x, y = pixel_width, pixel_length
    pass


def cut_images(in_dir: Path,
               out_dir: Path = None,
               n: int = 144):
    """Cut images in in_dir each into n smaller images. If n is a perfect square,
    will cut into equal rows and columns.

    :param in_dir: path to input image directory
    :param out_dir: directory to save cut images
    :param n: number of equal-sized images to cut out of each of the input images
    """
    if out_dir == None:
        out_dir = in_dir
    for jpg in sorted(in_dir.glob('*.jpg')):
        slice(jpg, n)
        if in_dir != out_dir:
            # move all sub-pngs to out_dir
            for png in sorted(in_dir.glob(jpg.stem + '_*.png')):
                print(png)
                name = png.name
                png.replace(out_dir / name)


def edit_geprint(lat: float, lon: float,
                 template_dirpath: Path,
                 save_image_quality: int=6,
                 altitude: float=634.,
                 template_filename: str='skybees_testconfig.geprint'):
    """Edit the template Google Earth print config file for new lat-lon location.

    :param lat: latitude of center of image to be downloaded
    :param lon: longitude of center of image to be downloaded
    :param save_image_quality: int to indicate image download resolution:
        - 0 resolution of the window
        - 1 1024x768
        - 2 1280x720
        - 3 1920x1080
        - 4 3840x2160
        - 5 8192x4320
        - 6 4800x4800
    :param altitude: emulated distance above ground of the image (basically how
        far to zoom in so the image looks like it was taken from X feet above ground).
    """


# MAIN -------------------------------
if __name__ == "__main__":
    # get_window()

    _BEECENSUS_DIR = Path(*Path.cwd().parts[:Path.cwd().parts.index('beecensus') + 1])
    _DATA_DIR = _BEECENSUS_DIR / 'data' / 'images'
    cut_images(_DATA_DIR / 'high-altitude',
               out_dir=_DATA_DIR / 'high-altitude-cut')
    # TODO: finish edit_geprint, and download all images at lat-lon in new-sat-download-latlons.xlsx
    # TODO: cut all images, sort into apiary and nonapiary
    # TODO: twice as many images in train as validation
    # TODO: run full training example, test how long it takes per image
    # TODO: train fRNCC on legacy tfrecord images and see how long it takes per image



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
    
    
NOTE ON GOOGLE EARTH IMAGE RIGHTS (from wiki, not actual source)    
Google asserts that every image created from Google Earth using satellite data provided by Google Earth is a copyrighted map. Any derivative from Google Earth is made from data on which Google claims copyright under United States Copyright Law. Google grants licenses in this data allowing, among other things, non-commercial personal use of the images (e.g., on a personal website or blog) as long as copyrights and attributions are preserved.[17] 
"""