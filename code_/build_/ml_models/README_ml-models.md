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









# References
Installation guide:
https://github.com/tensorflow/models/tree/master/official#running-the-models

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