# -*- coding: utf-8 -*-
"""

"""
import matplotlib.pyplot as plt
from skimage.io import imread
import numpy as np
import IPython.display as display
from PIL import Image
import pathlib
import os
# =============================================================================
# 
# data_dir= 'C:\\Users\\David\\Documents\\ULB\\MA1\\Projet_imagerie\\ISIC_2019_Training_Input'
# 
# for group in os.listdir(data_dir):
#     if 'txt' not in group:
#         for image_name in os.listdir(data_dir+group):
#             
# =============================================================================


def crop(file_path):
    image = imread(file_path)
#    plt.imshow(image)
#    plt.close()
    
    binary = image > 50
    binary = binary*255
    all_black=1
    for i in range(len(binary)):
        for pix in binary[i]:
            for j in pix:
                if j > 0:
                    all_black=0
                    break
        if not all_black:
            break
        image=np.delete(image,0,0)
    
    
    all_black=1
    for i in range(len(binary[0])):
        for pix in binary[:,i]:
            for j in pix:
                if j > 0:
                    all_black=0
        if not all_black:
            break
        image=np.delete(image,0,1)
    
    all_black=1
    for i in range(len(binary)-1,0,-1):
        for pix in binary[i]:
            for j in pix:
                if j > 0:
                    all_black=0
        if not all_black:
            break
        image=np.delete(image,len(image)-1,0)
    
    all_black=1
    for i in range(len(binary[0])):
        for pix in binary[:,-i]:
            for j in pix:
                if j > 0:
                    all_black=0
        if not all_black:
            break
        image=np.delete(image,len(image[0])-1,1)
#    plt.figure()
#    plt.imshow(image)
#    plt.close()
    im_name=file_path.split('\\')
    im_name[-2]+='_cropped'
    im_name = '\\'.join(im_name)
    plt.imsave(im_name,image)
    print(im_name+' saved')
    return(None)

images = os.listdir(r'C:\Users\David\Documents\ULB\MA1\Projet_imagerie\ISIC_2019_Training_Input\VASC')
for i in range(253):
    file_path = r'C:\Users\David\Documents\ULB\MA1\Projet_imagerie\ISIC_2019_Training_Input\VASC'+'\\'+images[i]
    crop(file_path)
    i+=1

    