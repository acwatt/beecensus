# Current Status
This project is in early development -- most of the project code still needs to be 
written. If you wish to contribute, see the project list below for the unassigned tasks.

### Project List
Tasks are organized by order in the pipeline.

| task                                                    | pipeline stage | contributor | status | associated readme             | associated scripts           |
| ------------------------------------------------------- | -------------- | ----------- | ------ | ----------------------------- | ---------------------------- |
| Shapefile cutting by landtype                           | 1.1            | DM          |        | [docs/gis/gis.md](gis/gis.md) | `code_/gis/county_latlon.py` |
| Shapefile to lat-lon grid                               | 1.2            |             |        |                               | `code_/build_/beehunter`, `code_/build_/googleearthdriver`                             |
| Download image via Google Earth                         | 2.1            | AW          | 60%    |                               |                              |
| Cut image into pieces                                   | 2.2            | AW          | 80%    |                               |                              |
| Classify image as yes/no apiary                         | 3.1            | AW          | 5%     |                               |                              |
| Detect apiary in image                                  | 3.2            | AW          | 5%     |                               |                              |
| Detect bee box in image                                 | 3.3            | AW          | 90%    |                               |                              |
| Add box data to box database                            | 4.1            |             |        |                               |                              |
| Correct for missing and incorrect identification issues | 4.2            |             |        |                               |                              |
| Calculate apiary statistics                             | 4.2            |             |        |                               |                              |
| Calculate geographical area statistics                  | 4.3            |             |        |                               |                              |


Contributors:
- Aaron Watt (AW)
- Darren Marotta (DM)


# Contributing to the Project
*Note*: there are many tools we will be using in this project
(python, Anaconda, PyCharm, GitHub, Amazing Web Services servers, 
etc.) so it may take some practice to get proficient. Once we set up
the basics with GitHub and PyCharm together, we will mostly be
focusing on writing the code and getting familiar with the GitHub 
tools. 

## First Steps:
1. Read about [object detection](https://www.datacamp.com/community/tutorials/object-detection-guide).
   
1. Finish reading through this document.
   
1. Skim [Ryan Kellogg's RA manual](https://github.com/kelloggrk/Kellogg_RA_Manual/wiki/Overview)
   (focus on the Project Management section).
   
1. If you haven't used Git before, read [this article](https://www.freecodecamp.org/news/learn-the-basics-of-git-in-under-10-minutes-da548267cc91/)
   or something similar to install Git. Make a practice repo and try commiting, 
   pushing, 
   pulling, and branching. PyCharm makes it easier to do these, but you 
   should understand how these basic commands work.
   
1. - install [Anaconda](https://www.anaconda.com/products/individual#Downloads)
   - Install [PyCharm community version](https://www.jetbrains.com/pycharm/download/#section=windows)
   - create a GitHub account if needed and send Aaron the username so he 
     can add you as a collaborator on the repository
   
1. Schedule time with Aaron to set up PyCharm and review GitHub repo.
   

## Background
### Project Background
Having good estimates of the the distribution of managed honey bees
in the United States is both intrinsically important to biologists
and also serves as an important input to other analyses. Current
estimates are expensive to administer and may have large unknown
sampling error because they rely on voluntary response. We wish to
verify these estimates by creating a US census of honey bee boxes
using free or low-cost satellite imagery and machine learning tools.

### Goals
- Build a dataset of honey bee box locations and apiary
  characteristics for the US using satellite imagery and several
  machine learning tools.
  
- Use the dataset to estimate statistics of the apiary and
  box distributions (e.g., county and state estimates).

### Organization
Borrowing ideas from [Ryan Kellogg's RA manual](https://github.com/kelloggrk/Kellogg_RA_Manual/wiki/Overview):
1. *End-to-end production*: we want to be able to reproduce 
   _everything_ we do by rerunning one script. During
   development, we may want to save intermediate data steps to
   increase speed, but we should always be able to go back and
   run everything from scratch.
   
1. *Replicable and shareable code*: We can share the code with
   others who ask about it using GitHub. Replication, however,
   means more than just giving people access to the GitHub repo
   and letting them look over the code. Replicability means 
   meaningful documentation. This will happen mainly in 
   comments inside of code and in README.md files inside some
   directories.

1. *Unambiguous process*: Keeping GitHub issues up to date 
   and folders free of half-finished or legacy files.

### GitHub & PyCharm
We will use GitHub issues to keep track of tasks (as layed out
in Kellogg's RA Manual) and branching, commits, and comments on 
commits to communicate. This may sound like a lot to learn but
it speeds up communication and production in major ways. Within code,
we can use `TODO:` comments to leave ourselves notes on what is left
to do in a specific script.

**Atomic commits**: A single commit should only contain a small change (e.g.
, "updated log in `this_function` to save more information about the 
process"). Do not mix different tasks into the same commit because it will 
cause issues if one of those tasks and not the other needs to be reverted. 
You can make edits to multiple parts of the code and PyCharm can help you 
choose which edits you would like to commit. It's easiest though to focus 
on one task at a time if possible and commit the edits when that task is 
complete.

### Python Programming Standards
When possible, we'll try to follow the [PEP-8 python style guide](https://pep8.org/).
PEP-8 offers a way to make sure our code is reasonably
formatted to allow other python programmers to read our code.
Some main style points:
- Try to stick to 80-100 characters per line -- it makes
  reading the code much easier. PyCharm has visual vertical guides for this.
  
- Document your code often using comments and docstrings. To start,
  write a docstring for every function. It can be just one sentence
  if it's obvious what the function does or a long description
  of inputs and outputs and typical results for more complicated
  functions / classes. See the [PEP-8 section on commenting](https://pep8.org/#comments)
  for tips on in-line comments.
  
- Documentation as the Single Source of Truth (SST): The SST methodology is 
  about using the documentation as your guide at each step of the programming. Start 
  by writing down the goals of the script (inputs, outputs, what transformations 
  need to be made, etc) and keep updating the documentation when you realize you 
  need to update your methods or add a step. For simplicity, you can keep temporary 
  documentation inside the docstring of the module or the function. If it provides 
  useful help to a future user or developer, move that documentation to a markdown 
  file in `docs/`.



## Tools being used
- python
  - TensorFlow library for machine learning models (some new, some already 
    trained).
  - Geopandas for converting geographical shape files into list of latitude 
    and longitude coordinates for downloading images.
  - [Code written by Robin Kiff](https://bitbucket.org/demandlinkdevelopment/beehunter/src/master/)
    to download images from google earth at all available dates for that
    location. This also includes some C# code.
    
- git
    - requires setting up an SSH key from your computer and adding to the 
      GitHub repository settings
    - can fully control all git functions through PyCharm (highly suggested 
      to use PyCharm for this because it has a great user interface for git)
      
- Google Earth pro (for downloading satellite images)
    
- barcode code written by David Sewell to add covariate barcodes to images. This 
  adds a barcode version of the time, location, geography, etc. to allow 
  the classification and object identification neural nets to encorporate more data 
  about the satellite images.