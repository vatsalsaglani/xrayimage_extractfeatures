

######
from .imports import *
from .glcms import *
from .helpers import *
from .moments import *
from .region_props import *
from tqdm import tqdm


def s_entropy(image):
    return shannon_entropy(image)


def entropy_simple(image):
    return entropy(image)


def feature_dict_from_imgpath(path, pat_id_array, getId=False):
    data_dict = dict()
    if getId == True:
        imgArray, _ids = extract_img_array(path, getID=True)
        for dc in tqdm(range(len(imgArray))):
            _g = glcm(imgArray[dc])
            _r = region_props(imgArray[dc])
            _m = moments(imgArray[dc])
            data_dict[pat_id_array[dc]] = [
                s_entropy(imgArray[dc]), entropy_simple(imgArray[dc]),
                _m.get_moments(), _m.get_HuMoments(), _r.max_area(),
                _r.eccentricity(), _r.euler_number(), _r.solidity(),
                _r.perimeter(), _r.mean_area(), _r.std_area(), _r.thresh_img(),
                _r.bb(), _r.bb_area(), _r.centroid_r(), _r.convex_area_r(), _r.coordinates_r(),
                _r.eq_diameter(), _r.extent_r(), _r.filled_area_r(), _r.inertia_tensor_r(),
                _r.inertia_tensor_eigvals_r(), _r.label_r(), _r.local_centroid_r(),
                _r.maj_ax_len(), _r.min_ax_len(), _r.orient(), _g.glcm_all()

            ]
        # return data_dict
    else:
        imgArray, _ids = extract_img_array(path)
        for dc in tqdm(range(len(imgArray))):
            _g = glcm(imgArray[dc])
            _r = region_props(imgArray[dc])
            _m = moments(imgArray[dc])
            data_dict[dc] = [
                s_entropy(imgArray[dc]), entropy_simple(imgArray[dc]),
                _m.get_moments(), _m.get_HuMoments(), _r.max_area(),
                _r.eccentricity(), _r.euler_number(), _r.solidity(),
                _r.perimeter(), _r.mean_area(), _r.std_area(), _r.thresh_img(),
                _r.bb(), _r.bb_area(), _r.centroid_r(), _r.convex_area_r(), _r.coordinates_r(),
                _r.eq_diameter(), _r.extent_r(), _r.filled_area_r(), _r.inertia_tensor_r(),
                _r.inertia_tensor_eigvals_r(), _r.label_r(), _r.local_centroid_r(),
                _r.maj_ax_len(), _r.min_ax_len(), _r.orient(), _g.glcm_all()

            ]
        # return data_dict

    return data_dict


def feature_dict_from_imgarray(imgArray, pat_id_array, getId=False):
    data_dict = dict()
    if getId == True:
        for dc in tqdm(range(len(imgArray))):
            _g = glcm(imgArray[dc])
            _r = region_props(imgArray[dc])
            _m = moments(imgArray[dc])
            data_dict[pat_id_array[dc]] = [
                s_entropy(imgArray[dc]), entropy_simple(imgArray[dc]),
                _m.get_moments(), _m.get_HuMoments(), _r.max_area(),
                _r.eccentricity(), _r.euler_number(), _r.solidity(),
                _r.perimeter(), _r.mean_area(), _r.std_area(), _r.thresh_img(),
                _r.bb(), _r.bb_area(), _r.centroid_r(), _r.convex_area_r(), _r.coordinates_r(),
                _r.eq_diameter(), _r.extent_r(), _r.filled_area_r(), _r.inertia_tensor_r(),
                _r.inertia_tensor_eigvals_r(), _r.label_r(), _r.local_centroid_r(),
                _r.maj_ax_len(), _r.min_ax_len(), _r.orient(), _g.glcm_all()

            ]
    else:
        for dc in tqdm(range(len(imgArray))):
            _g = glcm(imgArray[dc])
            _r = region_props(imgArray[dc])
            _m = moments(imgArray[dc])
            data_dict[dc] = [
                s_entropy(imgArray[dc]), entropy_simple(imgArray[dc]),
                _m.get_moments(), _m.get_HuMoments(), _r.max_area(),
                _r.eccentricity(), _r.euler_number(), _r.solidity(),
                _r.perimeter(), _r.mean_area(), _r.std_area(), _r.thresh_img(),
                _r.bb(), _r.bb_area(), _r.centroid_r(), _r.convex_area_r(), _r.coordinates_r(),
                _r.eq_diameter(), _r.extent_r(), _r.filled_area_r(), _r.inertia_tensor_r(),
                _r.inertia_tensor_eigvals_r(), _r.label_r(), _r.local_centroid_r(),
                _r.maj_ax_len(), _r.min_ax_len(), _r.orient(), _g.glcm_all()

            ]
    return data_dict


def get_df_from_path(path, pat_id_array, getId=False):
    if getId == True:
        data = feature_dict_from_imgpath(path, pat_id_array, getId=True)
    else:
        data = feature_dict_from_imgpath(path, pat_id_array)
    df = pd.DataFrame(data).T
    return df


def get_df_from_img_array(img_array, pat_id_array, getId=False):
    if getId == True:
        data = feature_dict_from_imgarray(img_array, pat_id_array, getId=True)
    else:
        data = feature_dict_from_imgarray(img_array, pat_id_array)
    df = pd.DataFrame(data).T
    return df
