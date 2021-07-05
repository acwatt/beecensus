# Python 3.7
# File name: main.py
# Authors: Aaron Watt, Darren Marotta
# Date: 2021-06-26
"""End-to-end script to build and analyze a dataset of bee box locations and
characteristics. Refer to README for project overview.
"""

# Standard library imports

# Third-party imports

# Local application imports
import findbees.build.utils.setup as setup
import findbees.build.ml_models.model_main as ml
from findbees.build.gis import latlon


# FUNCTIONS --------------------------
def end_to_end():
    """Run full script."""
    # Train various machine learning models for project (
    # ml.train_models()
    # Get Latitudes and Longitudes for chosen area (docs/gis/gis.md)
    # latlon_df = latlon.get_latlons()
    #



# MAIN -------------------------------
if __name__ == "__main__":
    end_to_end()



# REFERENCES -------------------------
"""

"""

# LICENSE -------------------------
"""
Copyright 2021 Aaron Watt, Darren Marotta

Permission is hereby granted, free of charge, to any person obtaining a copy of 
this software and associated documentation files (the "Software"), to deal in 
the Software without restriction, including without limitation the rights to use, 
copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the 
Software, and to permit persons to whom the Software is furnished to do so, 
subject to the following conditions:

The above copyright notice and this permission notice shall be included in all 
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR 
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS 
FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR 
COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER 
IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION 
WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
"""

