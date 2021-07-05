# Python 3.7
# File name: 
# Description: 
# Authors: Aaron Watt
# Date: 2021-06-26
"""Make sure all dependencies are installed via conda and pip"""

# Standard library imports
from pathlib import Path
import yaml

# Third-party imports
import urllib

# Local application imports
import tools

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
        self.code = self.root / 'code_'
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
        # Add the settings file to parse for other paths and settings
        self.settings_file = self.root / 'code_' / 'build_' / 'utils' / 'settings.csv'


class ProjectSettings:
    """Project class with settings from settings file and useful project paths."""
    def __init__(self):
        # Add paths inner class
        self.paths = Paths()
        self.add_settings()

    def add_settings(self):
        """For each setting listed in the settings file, add a setting attribute
        and value to the class instance.
        e.g. Project.geographical_name = "Philadelphia County, PA
        """
        d = tools.csv_to_dict(self.paths.settings_file)
        for key in d:
            setattr(self, key, d[key]['setting'])


# FUNCTIONS --------------------------
# This was used to download the model checkpoints used, but this is not in continuous use
def download_model_checkpoint(Project: ProjectSettings, model_type='ssd'):
    """Download the checkpoint and put it into data/checkpoints

    :return: pathlib Paths to model checkpoint folder and config file for model
    """
    model_dict = {
        'frcnn': 'http://download.tensorflow.org/models/object_detection/tf2/20200711/faster_rcnn_resnet50_v1_1024x1024_coco17_tpu-8.tar.gz',
        'ssd': 'http://download.tensorflow.org/models/object_detection/tf2/20200711/ssd_resnet50_v1_fpn_640x640_coco17_tpu-8.tar.gz'}
    url = model_dict[model_type]
    filename = Path(Path(url).name)
    # Make pretrained folder if it doensn't exist
    end_dir = Project.paths.root / 'data' / 'checkpoints' / 'pretrained'
    end_dir.mkdir(parents=True, exist_ok=True)
    # Remove extensions of zipped folder
    dirname = filename.with_suffix('').with_suffix('')
    model_path = end_dir / dirname
    if not (model_path.exists()):
        # Download the model checkpoint tarfile to the repo root
        print('Downloading model checkpoint tarball and unpacking...')
        tarpath = Project.paths.root / filename
        urllib.request.urlretrieve(url, tarpath)
        checkpoint_string = f'{filename}/checkpoint'
        # Extract the checkpoint folder to the checkpoints directory
        tar = tarfile.open(tarpath)
        members = [m for m in tar.getmembers() if checkpoint_string in m.path]
        tar.extractall(members=members, path=end_dir)
        tar.close()
        # Delete downloaded filed
        tarpath.unlink()
    model_config = Project.paths.models / 'research' / 'object_detection' / 'configs' / 'tf2' / f'{dirname}.config'
    return model_path, model_config



# MAIN -------------------------------
if __name__ == "__main__":
    Project = ProjectSettings()


# REFERENCES -------------------------
"""
Best Practices for building a config in Python:
https://tech.preferred.jp/en/blog/working-with-configuration-in-python/
"""
