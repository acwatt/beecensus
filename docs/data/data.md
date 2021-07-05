# checkpoints
### pretrained
tensorflow neural net checkpoints for models that have been pre-trained
on other datasets (like MS COCO). These are used as a starting point for fine-tune 
training of our models on our training data.

### finetuned
saved checkpoints of models that we have fine-tuned on our training 
data. These are applied to images during the search procedure to identify apiaries and 
bee boxes. 


# configs

### .pbtxt
A dictionary use in ML object identification to translate between the ID's of 
objects in images (like bee boxes) and the numbers that are used to represent them.

### .config
Config files for ML neural net creation and training. 

### .kml files
can specify tours in Google Earth -- a series of locations that GE views.

### .geprint files
Image configuration file: 
 - location:  
    `<longitude>-93.81981260476411</longitude>
   <latitude>30.75582863112696</latitude>`
 - date (can also extract this from a saved .geprint file after
   the date has been changed):  
   `<when>2014-11-26</when>`
 - altitide (need to set both range and alt):  
   `<altitude>500</altitude>` and `<range>0</range>`
 - tilt `<tilt>0</tilt>`
 - rotation (degrees E from N): `<heading>90</heading>`
 - ability to remove all other controls/boxes off of image:  
    `Layout\visible=false`


# images
Folders to hold various types of images. Used for training images for the 
classification and object detection neural network training.


# tables
Various lookup tables and datasets.


# temp
Temporary storage for files created, overwritten, and sometimes destroyed during the 
regular program usages and development. Files in here can be deleted without 
consequence as they can all be recreated from source code.


# test_data
Data used during development of the program and during example demonstrations.