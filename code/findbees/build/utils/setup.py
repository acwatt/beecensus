# Python 3.7
# File name: 
# Authors: Aaron Watt
# Date: 2021-06-26
"""Make sure all dependencies are installed via conda and pip"""

# Standard library imports
from pathlib import Path

# Third-party imports
import urllib
import tarfile

# Local application imports
from .config import Paths


# FUNCTIONS --------------------------
# This was used to download the model checkpoints used, but this is not in continuous use
## Could be used in a setup function that gets all data from original sources in
## a public version of this repo, where the repo doesn't host any of the data but after
## cloning, the setup function will get all data necessary before beginning the rest
## of the project run.
def download_model_checkpoint(paths: Paths, model_type='ssd'):
    """Download the checkpoint and put it into data/checkpoints

    :return: pathlib Paths to model checkpoint folder and config file for model
    """
    model_dict = {
        'frcnn': 'http://download.tensorflow.org/models/object_detection/tf2/20200711/faster_rcnn_resnet50_v1_1024x1024_coco17_tpu-8.tar.gz',
        'ssd': 'http://download.tensorflow.org/models/object_detection/tf2/20200711/ssd_resnet50_v1_fpn_640x640_coco17_tpu-8.tar.gz'}
    url = model_dict[model_type]
    filename = Path(Path(url).name)
    # Make pretrained folder if it doesn't exist
    end_dir = paths.root / 'data' / 'checkpoints' / 'pretrained'
    end_dir.mkdir(parents=True, exist_ok=True)
    # Remove extensions of zipped folder
    dirname = filename.with_suffix('').with_suffix('')
    model_path = end_dir / dirname
    if not (model_path.exists()):
        # Download the model checkpoint tarfile to the repo root
        print('Downloading model checkpoint tarball and unpacking...')
        tarpath = paths.root / filename
        urllib.request.urlretrieve(url, tarpath)
        checkpoint_string = f'{filename}/checkpoint'
        # Extract the checkpoint folder to the checkpoints directory
        tar = tarfile.open(tarpath)
        members = [m for m in tar.getmembers() if checkpoint_string in m.path]
        tar.extractall(members=members, path=end_dir)
        tar.close()
        # Delete downloaded filed
        tarpath.unlink()
    model_config = paths.models / 'research' / 'object_detection' / 'configs' / 'tf2' / f'{dirname}.config'
    return model_path, model_config


# MAIN -------------------------------


# REFERENCES -------------------------
"""

"""
