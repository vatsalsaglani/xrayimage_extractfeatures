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

def water_seg(image, footprint = np.ones((3,3))):
    distance = ndi.distance_transform_edt(image)
    local_maxi = peak_local_max(distance, indices=False, footprint=footprint, labels=image)
    markers = ndi.label(local_maxi)[0]
    labels = watershed(-distance, markers, mask = image)
    show(labels)