from .imports import *
from .helpers import *


class region_props:
    def __init__(self, image, sq=square(3)):
        self.image = image.astype('int64')
        self.thresh = threshold_otsu(self.image)
        self.bw = closing(self.image > self.thresh, sq)
        self.bw_clear = clear_border(self.bw)
        self.bw_label = label(self.bw_clear)
        self.regions = regionprops(self.bw_label)
        self.lista = []
        for e in self.regions:
            self.lista.append(e.area)
        _l = len(self.lista)
        if _l == 0:
            self.idx = -1
        else:
            _m = max(self.lista)
            self.idx = self.lista.index(_m)

    # shows the bw plot black and white patches

    def plot_show_bw(self):
        show(self.bw)

    # plots the black and other segmented areas

    def plot_image(self):
        show(self.bw_clear)

    # plots the black and other segemted areas as labels
    def plot_image_with_label(self):
        show(self.bw_label)

    # out of all the regions obtained from the image gives region area with the maximum area occupancy
    def max_area(self):
        _aa = max(self.lista, default = -1)
        if _aa == -1:
            return -1
        else:

            return max(self.lista)

    # gives the eccentricity of the max area region
    def eccentricity(self):
        if self.idx == -1:
            return -1
        # if len(self.lista) > 0:
            # return -1

        else:
            return self.regions[self.idx].eccentricity

    # gives the euler numner of the max area region
    def euler_number(self):
        if self.idx == -1:
            return -1
        # if len(self.lista) > 0:
            # return self.regions[self.idx].euler_number
        else:
            return -1

    # returns the solidity of the max area region
    def solidity(self):
        if self.idx == -1:
            return -1
        # if len(self.lista) > 0:
            # return self.regions[self.idx].solidity

        else:
            return -1

    # returns the perimeter of the max area region
    def perimeter(self):
        if self.idx == -1:
            return -1
        # if len(self.lista) > 0:
            # return self.regions[self.idx].perimeter

        else:
            return -1

    # returns the mean of all the areas of all the segmented regions
    def mean_area(self):
        if len(self.lista) > 0:
            return statistics.mean(self.lista)

        else:
            return -1

    # returns the standard deviation of areas of  all the segemnted regions
    def std_area(self):
        if len(self.lista) >= 2:
            return statistics.stdev(self.lista)
        else:
            return -1

    # returns the otsu threshold of the image
    def thresh_img(self):
        return self.thresh

    # returns the coordinates of the boundary box of the max area region
    def bb(self):
        if self.idx != -1:
            # if len(self.lista) > 0:
            return self.regions[self.idx].bbox

        else:
            return -1

    # returns the area of the boundary box.
    def bb_area(self):
        if self.idx != -1:
            # if len(self.lista) > 0:
            return self.regions[self.idx].bbox_area

        else:
            return -1

    # returns the centroid of the max area region
    def centroid_r(self):
        if self.idx != -1:
            # if len(self.lista) > 0:
            return self.regions[self.idx].centroid

        else:
            return -1

    # returns the convex area of the max area region
    def convex_area_r(self):
        if self.idx != -1:
            # if len(self.lista) > 0:
            return self.regions[self.idx].convex_area

        else:
            return -1

    # gives all the coordinates of the max area region
    def coordinates_r(self):
        if self.idx != -1:
            # if len(self.lista) > 0:
            return self.regions[self.idx].coords

        else:
            return -1

    # returns the equivalent diameter of the max area region
    def eq_diameter(self):
        if self.idx != -1:
        # if len(self.lista) > 0:
            return self.regions[self.idx].equivalent_diameter

        else:
            return -1

    def extent_r(self):
        if self.idx == -1:
            # if len(self.lista) > 0:
            return -1

        else:
            return self.regions[self.idx].extent

    # returns the filled area of the max area of the region
    def filled_area_r(self):
        if self.idx != -1:
            # if len(self.lista) > 0:
            return self.regions[self.idx].filled_area

        else:
            return -1

    # returns the inertia tensor of the max area region
    def inertia_tensor_r(self):
        if self.idx != -1:
            # if len(self.lista) > 0:
            return self.regions[self.idx].inertia_tensor

        else:
            return -1

    # returns the eigen values of the inertia tensor of the max area regions
    def inertia_tensor_eigvals_r(self):
        if self.idx != -1:
            # if len(self.lista) > 0:
            return self.regions[self.idx].inertia_tensor_eigvals

        else:
            return -1

    # returns the label of the region
    def label_r(self):
        if self.idx != -1:
            # if len(self.lista) > 0:
            return self.regions[self.idx].label

        else:
            return -1

    # returns the local centroid of the max area
    def local_centroid_r(self):
        if self.idx != -1:
            # if len(self.lista) > 0:
            return self.regions[self.idx].local_centroid

        else:
            return -1

    # returns the major axis length of the ellipse of the max area region
    def maj_ax_len(self):
        if self.idx != -1:
            # if len(self.lista) > 0:
            return self.regions[self.idx].major_axis_length

        else:
            return -1

    # returns the minor axis length of the ellips of the max area region
    def min_ax_len(self):
        if self.idx != -1:
            # if len(self.lista) > 0:
            return self.regions[self.idx].minor_axis_length

        else:
            return -1

    # returns the orientation
    def orient(self):
        if self.idx != -1:
            # if len(self.lista) > 0:
            return self.regions[self.idx].orientation

        else:
            return -1
