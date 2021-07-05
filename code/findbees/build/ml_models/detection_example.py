# Python 3.7
# File name: detection_example.py
# Description: example of tesnsorflow transfer learning object detection
# Authors: Aaron Watt
# Date: 2021-06-20
# This Example requires TF 2.5.

# Standard library imports
import os
import pathlib
import matplotlib
import matplotlib.pyplot as plt
import io
import scipy.misc
import numpy as np

# Third-party imports
from six import BytesIO
from PIL import Image, ImageDraw, ImageFont
from six.moves.urllib.request import urlopen

import tensorflow as tf
import tensorflow_hub as hub
from object_detection.utils import label_map_util
from object_detection.utils import visualization_utils as viz_utils
from object_detection.utils import ops as utils_ops

# Local application imports

# SETTINGS
tf.get_logger().setLevel('ERROR')



# FUNCTIONS --------------------------
## UTILITIES NEEDED LATER
def load_image_into_numpy_array(path):
  """Load an image from file into a numpy array.

  Puts image into numpy array to feed into tensorflow graph.
  Note that by convention we put it into a numpy array with shape
  (height, width, channels), where channels=3 for RGB.

  Args:
    path: the file path to the image

  Returns:
    uint8 numpy array with shape (img_height, img_width, 3)
  """
  image = None
  if(path.startswith('http')):
    response = urlopen(path)
    image_data = response.read()
    image_data = BytesIO(image_data)
    image = Image.open(image_data)
  else:
    image_data = tf.io.gfile.GFile(path, 'rb').read()
    image = Image.open(BytesIO(image_data))

  (im_width, im_height) = image.size
  return np.array(image.getdata()).reshape(
      (1, im_height, im_width, 3)).astype(np.uint8)




# MAIN -------------------------------
if __name__ == "__main__":
    # GLOBALS --------------------------
    # Needed for this example
    ALL_MODELS = {
        'CenterNet HourGlass104 512x512': 'https://tfhub.dev/tensorflow/centernet/hourglass_512x512/1',
        'CenterNet HourGlass104 Keypoints 512x512': 'https://tfhub.dev/tensorflow/centernet/hourglass_512x512_kpts/1',
        'CenterNet HourGlass104 1024x1024': 'https://tfhub.dev/tensorflow/centernet/hourglass_1024x1024/1',
        'CenterNet HourGlass104 Keypoints 1024x1024': 'https://tfhub.dev/tensorflow/centernet/hourglass_1024x1024_kpts/1',
        'CenterNet Resnet50 V1 FPN 512x512': 'https://tfhub.dev/tensorflow/centernet/resnet50v1_fpn_512x512/1',
        'CenterNet Resnet50 V1 FPN Keypoints 512x512': 'https://tfhub.dev/tensorflow/centernet/resnet50v1_fpn_512x512_kpts/1',
        'CenterNet Resnet101 V1 FPN 512x512': 'https://tfhub.dev/tensorflow/centernet/resnet101v1_fpn_512x512/1',
        'CenterNet Resnet50 V2 512x512': 'https://tfhub.dev/tensorflow/centernet/resnet50v2_512x512/1',
        'CenterNet Resnet50 V2 Keypoints 512x512': 'https://tfhub.dev/tensorflow/centernet/resnet50v2_512x512_kpts/1',
        'EfficientDet D0 512x512': 'https://tfhub.dev/tensorflow/efficientdet/d0/1',
        'EfficientDet D1 640x640': 'https://tfhub.dev/tensorflow/efficientdet/d1/1',
        'EfficientDet D2 768x768': 'https://tfhub.dev/tensorflow/efficientdet/d2/1',
        'EfficientDet D3 896x896': 'https://tfhub.dev/tensorflow/efficientdet/d3/1',
        'EfficientDet D4 1024x1024': 'https://tfhub.dev/tensorflow/efficientdet/d4/1',
        'EfficientDet D5 1280x1280': 'https://tfhub.dev/tensorflow/efficientdet/d5/1',
        'EfficientDet D6 1280x1280': 'https://tfhub.dev/tensorflow/efficientdet/d6/1',
        'EfficientDet D7 1536x1536': 'https://tfhub.dev/tensorflow/efficientdet/d7/1',
        'SSD MobileNet v2 320x320': 'https://tfhub.dev/tensorflow/ssd_mobilenet_v2/2',
        'SSD MobileNet V1 FPN 640x640': 'https://tfhub.dev/tensorflow/ssd_mobilenet_v1/fpn_640x640/1',
        'SSD MobileNet V2 FPNLite 320x320': 'https://tfhub.dev/tensorflow/ssd_mobilenet_v2/fpnlite_320x320/1',
        'SSD MobileNet V2 FPNLite 640x640': 'https://tfhub.dev/tensorflow/ssd_mobilenet_v2/fpnlite_640x640/1',
        'SSD ResNet50 V1 FPN 640x640 (RetinaNet50)': 'https://tfhub.dev/tensorflow/retinanet/resnet50_v1_fpn_640x640/1',
        'SSD ResNet50 V1 FPN 1024x1024 (RetinaNet50)': 'https://tfhub.dev/tensorflow/retinanet/resnet50_v1_fpn_1024x1024/1',
        'SSD ResNet101 V1 FPN 640x640 (RetinaNet101)': 'https://tfhub.dev/tensorflow/retinanet/resnet101_v1_fpn_640x640/1',
        'SSD ResNet101 V1 FPN 1024x1024 (RetinaNet101)': 'https://tfhub.dev/tensorflow/retinanet/resnet101_v1_fpn_1024x1024/1',
        'SSD ResNet152 V1 FPN 640x640 (RetinaNet152)': 'https://tfhub.dev/tensorflow/retinanet/resnet152_v1_fpn_640x640/1',
        'SSD ResNet152 V1 FPN 1024x1024 (RetinaNet152)': 'https://tfhub.dev/tensorflow/retinanet/resnet152_v1_fpn_1024x1024/1',
        'Faster R-CNN ResNet50 V1 640x640': 'https://tfhub.dev/tensorflow/faster_rcnn/resnet50_v1_640x640/1',
        'Faster R-CNN ResNet50 V1 1024x1024': 'https://tfhub.dev/tensorflow/faster_rcnn/resnet50_v1_1024x1024/1',
        'Faster R-CNN ResNet50 V1 800x1333': 'https://tfhub.dev/tensorflow/faster_rcnn/resnet50_v1_800x1333/1',
        'Faster R-CNN ResNet101 V1 640x640': 'https://tfhub.dev/tensorflow/faster_rcnn/resnet101_v1_640x640/1',
        'Faster R-CNN ResNet101 V1 1024x1024': 'https://tfhub.dev/tensorflow/faster_rcnn/resnet101_v1_1024x1024/1',
        'Faster R-CNN ResNet101 V1 800x1333': 'https://tfhub.dev/tensorflow/faster_rcnn/resnet101_v1_800x1333/1',
        'Faster R-CNN ResNet152 V1 640x640': 'https://tfhub.dev/tensorflow/faster_rcnn/resnet152_v1_640x640/1',
        'Faster R-CNN ResNet152 V1 1024x1024': 'https://tfhub.dev/tensorflow/faster_rcnn/resnet152_v1_1024x1024/1',
        'Faster R-CNN ResNet152 V1 800x1333': 'https://tfhub.dev/tensorflow/faster_rcnn/resnet152_v1_800x1333/1',
        'Faster R-CNN Inception ResNet V2 640x640': 'https://tfhub.dev/tensorflow/faster_rcnn/inception_resnet_v2_640x640/1',
        'Faster R-CNN Inception ResNet V2 1024x1024': 'https://tfhub.dev/tensorflow/faster_rcnn/inception_resnet_v2_1024x1024/1',
        'Mask R-CNN Inception ResNet V2 1024x1024': 'https://tfhub.dev/tensorflow/mask_rcnn/inception_resnet_v2_1024x1024/1'
    }

    IMAGES_FOR_TEST = {
        'Beach': 'models/research/object_detection/test_images/image2.jpg',
        'Dogs': 'models/research/object_detection/test_images/image1.jpg',
        # By Heiko Gorski, Source: https://commons.wikimedia.org/wiki/File:Naxos_Taverna.jpg
        'Naxos Taverna': 'https://upload.wikimedia.org/wikipedia/commons/6/60/Naxos_Taverna.jpg',
        # Source: https://commons.wikimedia.org/wiki/File:The_Coleoptera_of_the_British_islands_(Plate_125)_(8592917784).jpg
        'Beatles': 'https://upload.wikimedia.org/wikipedia/commons/1/1b/The_Coleoptera_of_the_British_islands_%28Plate_125%29_%288592917784%29.jpg',
        # By Américo Toledano, Source: https://commons.wikimedia.org/wiki/File:Biblioteca_Maim%C3%B3nides,_Campus_Universitario_de_Rabanales_007.jpg
        'Phones': 'https://upload.wikimedia.org/wikipedia/commons/thumb/0/0d/Biblioteca_Maim%C3%B3nides%2C_Campus_Universitario_de_Rabanales_007.jpg/1024px-Biblioteca_Maim%C3%B3nides%2C_Campus_Universitario_de_Rabanales_007.jpg',
        # Source: https://commons.wikimedia.org/wiki/File:The_smaller_British_birds_(8053836633).jpg
        'Birds': 'https://upload.wikimedia.org/wikipedia/commons/0/09/The_smaller_British_birds_%288053836633%29.jpg',
    }

    COCO17_HUMAN_POSE_KEYPOINTS = [(0, 1),
                                   (0, 2),
                                   (1, 3),
                                   (2, 4),
                                   (0, 5),
                                   (0, 6),
                                   (5, 7),
                                   (7, 9),
                                   (6, 8),
                                   (8, 10),
                                   (5, 6),
                                   (5, 11),
                                   (6, 12),
                                   (11, 12),
                                   (11, 13),
                                   (13, 15),
                                   (12, 14),
                                   (14, 16)]

    #### Load label map data (for plotting) ####
    # Label maps correspond index numbers to category names, so that when our
    # convolution network predicts 5, we know that this corresponds to airplane.
    # Here we use internal utility functions, but anything that returns a
    # dictionary mapping integers to appropriate string labels would be fine.
    #
    # We are going, for simplicity, to load from the repository that we loaded
    # the Object Detection API code
    PATH_TO_LABELS = './models/research/object_detection/data/mscoco_label_map.pbtxt'
    category_index = label_map_util.create_category_index_from_labelmap(
        PATH_TO_LABELS, use_display_name=True
    )

    #### Build a detection model and load pre-trained model weights ####
    # Here we will choose which Object Detection model we will use. Select the
    # architecture and it will be loaded automatically. If you want to change
    # the model to try other architectures later, just change the next cell
    # and execute following ones.
    #
    # Tip: if you want to read more details about the selected model, you can
    # follow the link (model handle) and read additional documentation on TF
    # Hub. After you select a model, we will print the handle to make it easier.
    model_display_name = 'CenterNet HourGlass104 Keypoints 512x512'
    model_handle = ALL_MODELS[model_display_name]
    print('Selected model:' + model_display_name)
    print(f'Model Handle at TensorFlow Hub: {model_handle}')

    # Loading the selected model from TensorFlow Hub¶
    # Here we just need the model handle that was selected and use the
    # Tensorflow Hub library to load it to memory.
    print('loading model...')
    hub_model = hub.load(model_handle)
    print('model loaded!')

    # Loading an image
    # Let's try the model on a simple image. To help with this, we provide a
    # list of test images.
    #
    # Here are some simple things to try out if you are curious:
    #
    # Try running inference on your own images, just upload them to colab and
    # load the same way it's done in the cell below.
    # Modify some of the input images and see if detection still works. Some
    # simple things to try out here include flipping the image horizontally,
    # or converting to grayscale (note that we still expect the input image to
    # have 3 channels).
    # Be careful: when using images with an alpha channel, the model expect 3
    # channels images and the alpha will count as a 4th.
    selected_image = 'Beach'  # @param ['Beach', 'Dogs', 'Naxos Taverna', 'Beatles', 'Phones', 'Birds']
    flip_image_horizontally = False  # @param {type:"boolean"}
    convert_image_to_grayscale = False  # @param {type:"boolean"}

    image_path = IMAGES_FOR_TEST[selected_image]
    image_np = load_image_into_numpy_array(image_path)

    # Flip horizontally
    if (flip_image_horizontally):
        image_np[0] = np.fliplr(image_np[0]).copy()

    # Convert image to grayscale
    if (convert_image_to_grayscale):
        image_np[0] = np.tile(
            np.mean(image_np[0], 2, keepdims=True), (1, 1, 3)).astype(np.uint8)
    # need to change the matplotlib backend back to the default
    # I think TF changes it to 'agg' to show things nicely in jupyter notebooks
    # but it does not allow for plotting through the console (qt5agg does)
    matplotlib.use('qt5agg')
    plt.figure(figsize=(24, 32))
    plt.imshow(image_np[0])
    plt.show()

    # Doing the inference
    # To do the inference we just need to call our TF Hub loaded model.
    #
    # Things you can try:
    #  - Print out result['detection_boxes'] and try to match the box locations
    #  to the boxes in the image. Notice that coordinates are given in normalized
    #  form (i.e., in the interval [0, 1]).
    #  - inspect other output keys present in the result. A full documentation
    #  can be seen on the models documentation page (pointing your browser
    #  to the model handle printed earlier)
    #
    # running inference
    results = hub_model(image_np)
    # different object detection models have additional results
    # all of them are explained in the documentation
    result = {key: value.numpy() for key, value in results.items()}
    print(result.keys())

    # Visualizing the results¶
    # Here is where we will need the TensorFlow Object Detection API to show
    # the squares from the inference step (and the keypoints when available).
    #
    # the full documentation of this method can be seen here
    # https://github.com/tensorflow/models/blob/master/research/object_detection/utils/visualization_utils.py
    # Here you can, for example, set min_score_thresh to other values (between
    # 0 and 1) to allow more detections in or to filter out more detections.
    label_id_offset = 0
    image_np_with_detections = image_np.copy()

    # Use keypoints if available in detections
    keypoints, keypoint_scores = None, None
    if 'detection_keypoints' in result:
        keypoints = result['detection_keypoints'][0]
        keypoint_scores = result['detection_keypoint_scores'][0]

    viz_utils.visualize_boxes_and_labels_on_image_array(
        image_np_with_detections[0],
        result['detection_boxes'][0],
        (result['detection_classes'][0] + label_id_offset).astype(int),
        result['detection_scores'][0],
        category_index,
        use_normalized_coordinates=True,
        max_boxes_to_draw=200,
        min_score_thresh=.30,
        agnostic_mode=False,
        keypoints=keypoints,
        keypoint_scores=keypoint_scores,
        keypoint_edges=COCO17_HUMAN_POSE_KEYPOINTS)

    plt.figure(figsize=(24, 32))
    plt.imshow(image_np_with_detections[0])
    plt.show()

# REFERENCES -------------------------
"""
TensorFlow Hub Object Detection Colab tutorial
- used for this example script
- the 'Colab code' was written to run in Google Colab, a cloud-based Google
computational service, but was easily adjusted for this script to run locally.
https://github.com/tensorflow/hub/blob/master/examples/colab/tf2_object_detection.ipynb
"""
