# Machine Learning sub-project goal
Inputs:
    - 

Output:
    - 

## Sub-project Procedure
1. 




# Setting up tensorflow models
1. Create a virtual environment so python installations don't ruin your other
   python systems. Always want something to roll back to (ie, the base 
   environment will always be there). We need to use python 3.7 (the latest 
   is 3.9) because some of the tools we need have not been updated to work 
   with python 3.8 or 3.9 yet.
   
   ```python
   conda create -n tf python=3.7 # create a conda environment called "tf"
   conda activate tf # switch to the tf environment to install packages
   ```

1. Since we have been using conda, we would normally use `conda install 
   <package-name>` to install python packages. However, we need to use 
   `pip` (another python package installer) 
   because conda doesn't have a recent enough version of
   `tensorflow` and `image_slicer` to work with windows. `pip` installs  
   python dependencies automatically.
   Install the following packages:
      - **TensorFlow**: for training, and applying the various
        machine learning models
      - **TensorFlow Model Garden**: for downloading and using specific models
      - **labelImg**: tool for creating object detection training data -- 
        drawing bounding boxes.
      - **image_slicer**: for cutting large, higher altitude images into 
        smaller images
   ```python
   # install tensorflow version 2.5+
   pip install tensorflow tf-models-official labelImg image_slicer
   ```
   You can run `labelImg` in the anaconda prompt, and it will open up the 
   image labeling program. If you start a new anaconda prompt, you will 
   have to activate your `tf` environment first with `conda activate tf`. 
   [labelImg documentation](https://pypi.org/project/labelImg/)
   
1. 

# Fine-tune a pre-existing object detection model
1. Install TensorFlow >= 2.5
   
1. Use labelImg.py to create XML labels on images.
   
1. Convert XML labels to CSV using 
1. Clone tensorflow model repo (currently in the `beecensus` repo)
   
1. Select the pre-trained model we want to base our training on.

1. Download the 
   
1. Copy that model's config file from 
   `models/research/object_detection/samples/configs` to `data/configs`
   
1. Edit config file to point at our 


## Editing the config file





# On choosing the pre-trained model to use
From Nhat-Duy Nguyen et al.:
> Because the amount of data will significant impact on the model, if data are 
> not abundant, the shallow network will fit it well.
>
> ... methods which belong to two-stage approaches
outperform ones in one-stage approaches about 8–10%.
Specifically, Faster RCNN with ResNeXT-101-64 × 4d-FPN
backbone achieved the top mAP in two-stage approaches
and the top of the table as well, 41.2%. In comparison with
the top in one-stage approaches, YOLOv3 608 × 608 with
Darknet-53 obtained 33.1%. Following [32], methods based
on region proposal such as Faster RCNN are better than
methods based on regression or classification such as YOLO
and SSD.

It appears that the best choice for a pre-trained model to use and 
fine-tune would be something based on Faster RCNN.





# References
Installation guide:
https://github.com/tensorflow/models/tree/master/official#running-the-models

Nhat-Duy Nguyen et al., “An Evaluation of Deep Learning Methods for Small Object Detection,” Journal of Electrical and Computer Engineering 2020 (April 27, 2020): e3189691, https://doi.org/10.1155/2020/3189691.

## Citing TF Official Model Garden
To cite this repository:
```
@software{tfmodels2020github,
  author = {Chen Chen and Xianzhi Du and Le Hou and Jaeyoun Kim and Jing Li and
  Yeqing Li and Abdullah Rashwan and Fan Yang and Hongkun Yu},
  title = {TensorFlow Official Model Garden},
  url = {https://github.com/tensorflow/models/tree/master/official},
  year = {2020},
}
```