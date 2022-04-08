
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
    imgObj = nib.Nifti1Image(new_img,maskObj.affine)
    nib.save(imgObj,'{subjects_dir}/{subj}/mri/{out_name}'.format(subjects_dir=subjects_dir,
                                                                                subj=subj,
                                                                                out_name=out_name))

def susan(input_img): 
    input_img = input_img.split('.nii')[0]
    cmd='susan {input_img}.nii.gz 1 1 3 1 0 {input_img}_susan.nii.gz'.format(input_img = input_img)
    out,err = run_cmd(cmd)
    
## functions for running unix cmd
# unix command
def unix_cmd(cmd):
    p=subprocess.Popen(cmd,stdout=subprocess.PIPE,stderr=subprocess.PIPE,shell=True)
    out,err=p.communicate()
    return out,err

def show_error(err):
    if len(err) > 0: 
        print(err)
        

# reading the T1 volume under freesurfer

T1 = nib.load('{subjects_dir}/{subj}/mri/T1.mgz'.format(subjects_dir=subjects_dir,subj=subj)).get_data()


# creating a mask for both ventricles and choroid plexus: 
print 'Creating masks: choroid+ventricle.mgz and aseg_choroid.mgz'

cmd = 'mri_binarize --i {subjects_dir}/{subj}/mri/aseg.mgz --match 31 63  --o {subjects_dir}/{subj}/mri/aseg_choroid_mask.nii.gz'
cmd = cmd.format(subjects_dir=subjects_dir, subj=subj)
run_cmd(cmd)


cmd = 'mri_binarize --i {subjects_dir}/{subj}/mri/aseg.mgz --match 4 5 31  --o {subjects_dir}/{subj}/mri/lh_choroid+ventricle_mask.nii.gz'
cmd = cmd.format(subjects_dir=subjects_dir, subj=subj)
run_cmd(cmd)

cmd = 'mri_binarize --i {subjects_dir}/{subj}/mri/aseg.mgz --match 43 44 63  --o {subjects_dir}/{subj}/mri/rh_choroid+ventricle_mask.nii.gz'
cmd = cmd.format(subjects_dir=subjects_dir, subj=subj)
run_cmd(cmd)


### left hemisphere (lh)
# get the intensity values for the mask:

print 'getting intensity values for the mask ....'

maskObj = nib.load('{subjects_dir}/{subj}/mri/lh_choroid+ventricle_mask.nii.gz'.format(subjects_dir=subjects_dir,
                                                                        subj=subj))
mask = maskObj.get_data()
mask_indices = np.where(mask==1)
mask_indices_array = np.array(mask_indices)
mask_T1_vals = T1[mask_indices]


X = np.reshape(mask_T1_vals,(-1,1))
gmmb = BayesianGaussianMixture(n_components=2, covariance_type='full').fit(X)

save_segmentation(gmmb,'lh_choroid_gmmb_mask.nii.gz')


## susan 
input_img = '{subjects_dir}/{subj}/mri/lh_choroid_gmmb_mask.nii.gz'.format(subjects_dir=subjects_dir,subj=subj)
susan(input_img)

## read choroid_gmmb_mask_susan.nii.gz
choroid_gmmb_mask = nib.load('{subjects_dir}/{subj}/mri/lh_choroid_gmmb_mask.nii.gz'.format(subjects_dir=subjects_dir, subj=subj))
choroid_gmmb_mask_ = choroid_gmmb_mask.get_data()