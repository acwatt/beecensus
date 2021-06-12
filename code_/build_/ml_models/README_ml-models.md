# Setting up tensorflow models
1. Create a virtual environment so python installations don't ruin your other
   python systems. Always want something to roll back to (ie, the base 
   environment will always be there).
   
   ```python
   conda create -n tf # create a conda environment called "tf"
   conda activate tf # switch to the tf environment to install packages
   ```

1. Need to use pip because conda doesn't have recent enough version of
   tensorflow to work with windows and python versions.
   ```python
   pip install tensorflow # should install tensorflow version 2.5+
   ```

1. Install the TensorFlow Model Garden pip package

   tf-models-official is the stable Model Garden package. 
   pip will install all models and dependencies automatically.
   ```python
   pip install tf-models-official
   ```   

1. Install the `labelImg` tool for creating training data (drawing bounding 
   boxes)
   
   ```
   pip install labelImg
   ```
   You can run `labelImg` in the anaconda prompt, and it will open up the 
   image labeling program. If start a new anaconda prompt, you will have to 
   activate your `tf` environment first with `conda activate tf`. [labelImg 
   documentation](https://pypi.org/project/labelImg/)

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