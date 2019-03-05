# all import statements
# from xtract_features.imports import *

from .imports import *

class moments:
    
    def __init__(self, image):
        self.image = image
        self.moment = cv2.moments(self.image)
        self.hu = cv2.HuMoments(self.moment)
        
    def get_moments(self):
#         keys = [key for key in self.moment.keys()]
        values = [value for value in self.moment.values()]
        return values
    
    def get_HuMoments(self):
        moments_hu = []
        for m in range(len(self.hu)):
            moments_hu.append(self.hu[m][0])
        return moments_hu