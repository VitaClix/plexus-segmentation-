
### ChP-Seg: A lightweight python script for accurate segmentation of choroid plexus 
## Author: Ehsan Tadayon, MD
## Date: 2019

import numpy as np
import nibabel as nib
from sklearn.mixture import GaussianMixture,BayesianGaussianMixture
import sys
import subprocess

### parameters
subjects_dir= sys.argv[1]
subj = sys.argv[2]

### functions

def run_cmd(cmd):
    print cmd
    out,err = unix_cmd(cmd)
    print out
    show_error(err)