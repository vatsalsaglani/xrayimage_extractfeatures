# from xtract_features.imports import *
from .imports import *
# kernels

# 1. Identity Kernel

identity_k = np.array([
    [0, 0, 0],
    [0, 1, 0],
    [0, 0, 0]
])

# 2. Edge Detection Kernel

edgeall_k = np.array([
    [0, -1, 0],
    [-1, 4, -1],
    [0, -1, 0]
])

edgeH_k = np.array([
    [0, 0, 0],
    [-1, 2, -1],
    [0, 0, 0]
])

edgeV_k = np.array([
    [0, -1, 0],
    [0, 2, 0],
    [0, -1, 0]
])

# 3. Sharpness Kernel

sharp_k = np.array([
    [0, -1, 0],
    [-1, 5, -1],
    [0, -1, 0]
])

# 4. Gaussian Blur Kernel

gauss3_k = np.array([
    [1, 2, 1],
    [2, 4, 2],
    [1, 2, 1]
])

gauss5_k = (1/256)*np.array([
    [1, 4, 6, 4, 1],
    [4, 16, 24, 16, 4],
    [6, 24, 36, 24, 6],
    [4, 16, 24, 16, 4],
    [1, 4, 6, 4, 1]
])

# 5. Box Blur Kernel

boxblur_k = np.array([
    [1, 1, 1],
    [1, 1, 1],
    [1, 1, 1]
])

# 6. Unsharp Masking Kernel

unsharpmask_k = (-1/256)*np.array([
    [1, 4, 6, 4, 1],
    [4, 16, 24, 16, 4],
    [6, 24, -476, 24, 6],
    [4, 16, 24, 16, 4],
    [1, 4, 6, 4, 1]
])

# 7. Gradient detection Kernel

gradH_k = np.array([
    [-1, -1, -1],
    [0, 0, 0],
    [1, 1, 1]
])

gradV_k = np.array([
    [-1, 0, 1],
    [-1, 0, 1],
    [-1, 0, 1]
])

# 8. Sobel Features Kernel

sobelH_k = np.array([
    [1, 2, 1],
    [0, 0, 0],
    [-1, -2, -1]
])

sobelV_k = np.array([
    [1, 0, -1],
    [2, 0, -2],
    [1, 0, -1]
])

# 9. Emboss Kernel

emboss_k = np.array([
    [-2, -2, 0],
    [-2, 6, 0],
    [0, 0, 0]
])

kernel_dict = {"identity": identity_k, "edge-all": edgeall_k, "edge-H": edgeH_k, "edge-V": edgeV_k,
               "sharp": sharp_k, "gauss-3": gauss3_k, "gauss-5": gauss5_k, "boxblur": boxblur_k,
               "unsharp": unsharpmask_k, "gradient-H": gradH_k, "gradient-V": gradV_k, "sobel-H": sobelH_k,
               "sobel-V": sobelV_k, "emboss": emboss_k
               }


def conv2d(img, ker_name, name=None):
    kernel = kernel_dict[ker_name]
    img = img[newaxis, :, :]
    for x in range(len(img)):
        conv = convolve2d(img[x, :, :], kernel, mode='same')
        plt.axis('off')
        plt.imshow(conv, cmap='gray')
        if name is not None:
            plt.savefig(str(name)+'.png', bbox_inches='tight')
    return conv
