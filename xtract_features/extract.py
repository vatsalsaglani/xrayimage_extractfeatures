# from imports import *
from glcms import *
from region_props import *
from moments import *
# from helpers import extract_img_array

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

def save_pickle(file, file_name):
    with open(file_name, "wb") as fp:
        pickle.dump(file, fp)


# load the saved pickle files.
# arguments: name of the file

def load_pickle(file_name):
    with open(file_name, "rb") as fp:
        file =  pickle.load(fp)
    return file

def plots(ims, figsize=(12,6), rows=2, titles=None):
    f = plt.figure(figsize=figsize)
    cols = len(ims)//rows
    for i in range(len(ims)):
        sp = f.add_subplot(rows, cols, i+1)
        sp.axis('Off')
        if titles is not None: sp.set_title(titles[i], fontsize=16)
        plt.imshow(ims[i], cmap=plt.cm.bone)



def s_entropy(image):
    return shannon_entropy(image)


def entropy_simple(image):
    return entropy(image)


def feature_dict_from_imgpath(path, pat_id_array, getId = False):
    data_dict = dict()
    if getId == True:
        imgArray, _ids = extract_img_array(path, getID=True)
        for dc in range(len(imgArray)):
            _g = glcm(imgArray[dc])
            _r = region_props(imgArray(dc))
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
        for dc in range(len(imgArray)):
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
        for dc in range(len(imgArray)):
            _g = glcm(imgArray[dc])
            _r = region_props(imgArray(dc))
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
        for dc in range(len(imgArray)):
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


def get_df_from_path(path, pat_id_array, getId = False):
    if getId == True:
        data = feature_dict_from_imgpath(path, getId=True, pat_id_array)
    else:
        data = feature_dict_from_imgpath(path, pat_id_array)
    df = pd.DataFrame(data)
    return df

def get_df_from_img_array(img_array,pat_id_array, getId = False):
    if getId == True:
        data = feature_dict_from_imgarray(img_array,pat_id_array, getId=True)
    else:
        data = feature_dict_from_imgarray(img_array, pat_id_array)
    df = pd.DataFrame(data)
    return df
    
