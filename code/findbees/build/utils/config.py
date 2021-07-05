# Python 3.7
# File name: 
# Authors: Aaron Watt
# Date: 2021-07-05
"""Module to be imported for project settings."""

# Standard library imports
from pathlib import Path

# Third-party imports

# Local application imports
from . import tools


# CLASSES --------------------------
class Paths:
    """Inner paths class to store project paths commonly used.

    This will search the current working directory path for the name of the
    repo (beecensus). Since this code is only called from main.py, and main.py
    is inside the repo, it should be able to find the beecensus path.
    This also means the name of the repo cannot be changed.
    Since this is an inner class, paths will be accessible in the following way:
    Project = ProjectSettings()  # instance of the outer class
    Project.paths.root  # this will be the pathlib path to the github repo root
    """
    def __init__(self):
        # add root path of the project / git repo
        self.root = Path(*Path.cwd().parts[:Path.cwd().parts.index('beecensus') + 1])
        # Top-level paths
        self.code = self.root / 'code'
        self.docs = self.root / 'docs'
        self.models = self.root / 'models'
        self.output = self.root / 'output'
        self.paper = self.root / 'paper'
        # Data directories
        self.data = self.root / 'data'
        self.checkpoints = self.data / 'checkpoints'
        self.configs = self.data / 'configs'
        self.images = self.data / 'images'
        self.tables = self.data / 'tables'
        self.temp = self.data / 'temp'


class GISSettings:
    """Class to hold settings for gis portion of project.

    Possible geographical names:
        - Philadelphia County, PA
    """
    def __init__(self):
        # Name of geographical area to be used in the search for bees.
        self.geographical_name = 'Philadelphia County, PA'


class MLSettings:
    """Class to hold settings for machine learning portion of project.

    Model names are tensorflow model names used in fetching the model checkpoint.
    Possible Classifier models:
        - resent50

    Possible Object Detector models:
        - faster_rcnn_resnet50_v1_1024x1024_coco17_tpu-8
        - ssd_mobilenet_v2_320x320_coco17_tpu-8
    """
    def __init__(self):
        # Model to be used as a base in classifying images as having or not having bee boxes.
        self.ml_classifier_name = 'resnet50'
        # Model to be used as a base in training the detection of apiaries in images.
        self.ml_apiary_detector_name = 'faster_rcnn_resnet50_v1_1024x1024_coco17_tpu-8'
        # Model to be used as a base in training the detection of bee boxes in images.
        self.ml_box_detector_name = 'faster_rcnn_resnet50_v1_1024x1024_coco17_tpu-8'


class GoogleEarthDriverSettings:
    """Class to hold settings for controlling Google Earth when downloading images."""
    def __init__(self):
        pass


# FUNCTIONS --------------------------


# MAIN -------------------------------
# Create instances of each class to be called from other
PATHS = Paths()
GIS = GISSettings()
ML = MLSettings()
GE = GoogleEarthDriverSettings()


# REFERENCES -------------------------
"""

"""
