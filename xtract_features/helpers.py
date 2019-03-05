# extract image from array,
# arguments: path to image files

# from imports import *
# all import statements
import numpy as np
import pandas as pd
import pydicom as pyd
import os
import matplotlib.pyplot as plt
# import mudicom
import scipy
import pickle
import cv2
import math
import statistics

from numpy import newaxis
from numpy import array
from os.path import dirname, join
# from pydicom.data import get_testdata_files
# from pydicom.filereader import read_dicomdir
from PIL import Image
from scipy.misc import imresize
from scipy.signal import convolve2d
from skimage.segmentation import slic, mark_boundaries, clear_border
from skimage.measure import label, regionprops
from skimage.filters import threshold_otsu
from skimage.morphology import closing, square
from skimage.color import label2rgb
from scipy import ndimage as ndi
from skimage.morphology import watershed
from skimage.feature import peak_local_max
from skimage.measure import shannon_entropy
from skimage import io, color, img_as_ubyte
from skimage.feature import greycomatrix, greycoprops
from sklearn.metrics.cluster import entropy


def extract_img_array(path, getID = False):
    lst_files = []
    for dir_name, sub_dir_list, file_list in os.walk(path):
        for file_name in file_list:
            if ".dcm" in file_name.lower():
                lst_files.append(os.path.join(dir_name, file_name))
    dcm_np = []
    _ids = []
    for dcm in lst_files:
        img = pyd.dcmread(dcm)
        img = pyd.pixel_array
        dcm_np.append(img)
        if getID == True:
            _ids.append(dcm.split('/')[1].split('.')[0])

    return dcm_np, _ids


#save files/list/ any datastructure to pickle file.
# arguments: variable containing the data structure and desired name to save
def save_pickle(file, file_name):
    with open(file_name, "wb") as fp:
        pickle.dump(file, fp)


# load the saved pickle files.
# arguments: name of the file

def load_pickle(file_name):
    with open(file_name, "rb") as fp:
        file =  pickle.load(fp)
    return file

# show plot

def show(img, title=None):
    plt.imshow(img, cmap=plt.cm.bone)
    if title is not None: plt.title = title


# show multiple plots

def plots(ims, figsize=(12,6), rows=2, titles=None):
    f = plt.figure(figsize=figsize)
    cols = len(ims)//rows
    for i in range(len(ims)):
        sp = f.add_subplot(rows, cols, i+1)
        sp.axis('Off')
        if titles is not None: sp.set_title(titles[i], fontsize=16)
        plt.imshow(ims[i], cmap=plt.cm.bone)



        