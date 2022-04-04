
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
    return out,err
    
def save_segmentation(clf,out_name):
    new_img = np.zeros((256,256,256))

    #choroid_ind = np.where(np.mean(clf.means_)==np.max(clf.means_))

    if np.mean(mask_T1_vals[clf.predict(X)==1]) > np.mean(mask_T1_vals[clf.predict(X)==0]): 
    
        choroid_ind = np.where(clf.predict(X)==1)[0]
    else: 

        choroid_ind = np.where(clf.predict(X)==0)[0]

    choroid_coords = (mask_indices[0][choroid_ind], mask_indices[1][choroid_ind], mask_indices[2][choroid_ind])
    new_img[choroid_coords] = 1