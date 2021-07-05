# Python 3.7
# File name: 
# Description: 
# Authors: Aaron Watt
# Date: 2021-06-20

# Standard library imports
import os
import glob
import pandas as pd
from pathlib import Path

# Third-party imports
import xml.etree.ElementTree as ET

# Local application imports

# FUNCTIONS --------------------------
def xml_to_csv(path):
    xml_list = []
    for xml_file in path.glob('*.xml'):
        tree = ET.parse(xml_file)
        root = tree.getroot()
        for member in root.findall('object'):
            value = (root.find('filename').text,
                     int(root.find('size')[0].text),
                     int(root.find('size')[1].text),
                     member[0].text,
                     int(member[4][0].text),
                     int(member[4][1].text),
                     int(member[4][2].text),
                     int(member[4][3].text)
                     )
            xml_list.append(value)
    column_name = ['filename', 'width', 'height', 'class', 'xmin', 'ymin', 'xmax', 'ymax']
    xml_df = pd.DataFrame(xml_list, columns=column_name)
    return xml_df


def main():
    """Convert XML annotations from labelImg.py to a csv of bounding boxes to be
    used by TensorFlow.

    If we want to have separate train, test (or validation) directories:
    for directory in ['train','test']:
        image_path = os.path.join(os.getcwd(), 'images/{}'.format(directory).format(directory))
        xml_df = xml_to_csv(image_path)
        xml_df.to_csv('data/{}_labels.csv'.format(directory), index=None)
        print('Successfully converted xml to csv.')
    """
    github_path = Path(*Path.cwd().parts[:Path.cwd().parts.index('beecensus') + 1])
    xml_path = github_path / 'data' / 'annotations' / 'xml'
    xml_df = xml_to_csv(xml_path)
    xml_df.to_csv(github_path / 'data' / 'annotations' / 'csv' / 'train_labels.csv', index=None)


# MAIN -------------------------------
if __name__ == "__main__":
    main()

# REFERENCES -------------------------
"""
https://towardsdatascience.com/custom-object-detection-using-tensorflow-from-scratch-e61da2e10087
"""
