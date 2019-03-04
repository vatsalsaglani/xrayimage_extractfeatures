# from imports import *
from helpers import show

class region_props:
    def __init__(self, image, sq = square(3)):
        self.image = image.astype('int64')
        self.thresh = threshold_otsu(self.image)
        self.bw = closing(self.image > self.thresh, sq)
        self.bw_clear = clear_border(self.bw)
        self.bw_label = label(self.bw_clear)
        self.regions = regionprops(self.bw_label)
        self.lista = []
        for e in self.regions:
            self.lista.append(e.area)
        self.idx = self.lista.index(max(self.lista))


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
        return max(self.lista)
    
    # gives the eccentricity of the max area region
    def eccentricity(self):
        return self.regions[self.idx].eccentricity
    
    # gives the euler numner of the max area region
    def euler_number(self):
        return self.regions[self.idx].euler_number
    
    # returns the solidity of the max area region
    def solidity(self):
        return self.regions[self.idx].solidity
    
    # returns the perimeter of the max area region
    def perimeter(self):
        return self.regions[self.idx].perimeter
    
    # returns the mean of all the areas of all the segmented regions
    def mean_area(self):
        return statistics.mean(self.lista)
    
    # returns the standard deviation of areas of  all the segemnted regions
    def std_area(self):
        if len(self.lista)>=2:
            return statistics.stdev(self.lista)
        else:
            return -1
    
    # returns the otsu threshold of the image
    def thresh_img(self):
        return self.thresh
    
    # returns the coordinates of the boundary box of the max area region
    def bb(self):
        return self.regions[self.idx].bbox
    
    # returns the area of the boundary box.
    def bb_area(self):
        return self.regions[self.idx].bbox_area
    
    # returns the centroid of the max area region
    def centroid_r(self):
        return self.regions[self.idx].centroid
    
    # returns the convex area of the max area region
    def convex_area_r(self):
        return self.regions[self.idx].convex_area
    
    # gives all the coordinates of the max area region
    def coordinates_r(self):
        return self.regions[self.idx].coords
    
    # returns the equivalent diameter of the max area region
    def eq_diameter(self):
        return self.regions[self.idx].equivalent_diameter
    
    
    def extent_r(self):
        return self.regions[self.idx].extent
    
    # returns the filled area of the max area of the region
    def filled_area_r(self):
        return self.regions[self.idx].filled_area
    
    # returns the inertia tensor of the max area region
    def inertia_tensor_r(self):
        return self.regions[self.idx].inertia_tensor
    
    # returns the eigen values of the inertia tensor of the max area regions
    def inertia_tensor_eigvals_r(self):
        return self.regions[self.idx].inertia_tensor_eigvals
    
    # returns the label of the region
    def label_r(self):
        return self.regions[self.idx].label
    
    # returns the local centroid of the max area
    def local_centroid_r(self):
        return self.regions[self.idx].local_centroid
    
    # returns the major axis length of the ellipse of the max area region
    def maj_ax_len(self):
        return self.regions[self.idx].major_axis_length
    
    # returns the minor axis length of the ellips of the max area region
    def min_ax_len(self):
        return self.regions[self.idx].minor_axis_length
    
    # returns the orientation
    def orient(self):
        return self.regions[self.idx].orientation