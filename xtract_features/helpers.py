# extract image from array,
# arguments: path to image files

# from imports import *
# all import statements
from xtract_features.imports import *

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



        