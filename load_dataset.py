"""-----------------------------------------
step 2:
     Load all photos and tags in the dataset;
     Function return value list: all picture collection, label collection, label number;
----------------------------------------- """
# -*-coding:utf8-*-
import os
import cv2
import numpy as np

from read_img import endwith

"""
Enter a file path, read the pictures under each folder, and give each folder a different Label;
Return a list of img, return a list corresponding to the label, return a few folders (with several labels);
If there are multiple folders under the dataset, each folder name corresponds to a label;
"""
def read_file(path):
    # Picture collection
    img_list = []
    # Label collection
    label_list = []
    # The number of subfolders, that is, the number of labels
    label_num = 0
    # size of the picture
    IMG_SIZE = 128

    # Read and save all jpg files in all subfolders under the path to a list
    for child_dir in os.listdir(path):
        child_path = os.path.join(path, child_dir)

        for dir_image in os.listdir(child_path):
            if endwith(dir_image, 'jpg'):
                img = cv2.imread(os.path.join(child_path, dir_image))
                resized_img = cv2.resize(img, (IMG_SIZE, IMG_SIZE))
                recolored_img = cv2.cvtColor(resized_img, cv2.COLOR_BGR2GRAY)
                img_list.append(recolored_img)
                label_list.append(label_num)
        # label number increment
        label_num += 1

    # The returned img_list is converted to np.array format
    img_list = np.array(img_list)

    # Return value list: all pictures collection, label collection, label number
    return img_list, label_list, label_num


# Read the folders under the training data set and return their names, ie labels, to a list
def read_name_list(path):
    name_list = []
    for child_dir in os.listdir(path):
        name_list.append(child_dir)
    return name_list


if __name__ == '__main__':
    img_list, label_lsit, label_num = read_file('./dataset')
    # Print the number of labels
    print(label_num)
    print(label_lsit)
