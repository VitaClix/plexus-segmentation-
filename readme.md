# Improved Choroid Plexus Segmentation using Gaussian Mixture Models (GMM)

This repository focuses on the study of choroid plexus and its crucial role in CSF-based clearance systems. The transported CSF proteins including Aβ to the blood by transporter lined epithelium of the choroid plexus. The non-invasive imaging technique for this study is T1-weighted MRIs. Prior to this, Freesurfer was used for automatic choroid plexus segmentation but the limitation was improved using Gaussian Mixture Models (GMM) which gave more accurate results. We've tried & tested this algorithm extensively against manual segmentations as well as Freesurfer. 

## Citation

Our paper describing this lightweight algorithm with potential implications for multi-modal neuroimaging studies of choroid plexus in dementia is published. If you use ChP-GMM segmentation, please cite our paper: 

> Improving Choroid Plexus Segmentation in the Healthy and Diseased Brain: Relevance for Tau-PET Imaging in Dementia. Journal of Alzheimer's Disease


## Pipeline

![Pipeline](./docs/pipeline.png)

## Comparing GMM and Freesurfer against Manual Segmentation (MS) in 20 subjects of Human Connectome Project (HCP) dataset

![Performance](./docs/performance.png)

## Choroid plexus segmentation for three representative subjects of HCP dataset using Freesurfer and GMM

![Samples](./docs/samples.png)

## Required packages

- FSL
- Freesurfer
- Python: nibabel, sklearn, numpy 

## How to run the 