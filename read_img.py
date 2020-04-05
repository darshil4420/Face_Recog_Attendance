"""-----------------------------------------
step 1: Define the function for loading photos;
         Load all photos from the source folder, the format of the photos can be specified by the parameter * suffix,
     The return value is a list;
----------------------------------------- """
# -*-coding:utf8-*-
import os
import cv2

"""
According to the input folder path, read and save all the specified suffix files in the folder into a list
———— The first element of the list is the name of the folder
"""
def readAllImg(path, *suffix):
    try:
        s = os.listdir(path)
        resultArray = []
        fileName = os.path.basename(path)
        resultArray.append(fileName)

        for i in s:
            if endwith(i, suffix):
                document = os.path.join(path, i)
                img = cv2.imread(document)
                resultArray.append(img)


    except IOError:
        print("Error")

    else:
        print("Read successfully")
        # Return a list with all the pictures in the path
        return resultArray


# Enter a string and a tag, and match the subsequent string with the tag
# * endstring is the file suffix name: such as jpg, png, etc.
def endwith(s, *endstring):
    resultArray = map(s.endswith, endstring)
    if True in resultArray:
        return True
    else:
        return False

if __name__ == '__main__':
    result = readAllImg("./dataset", '.jpg', '.png')
    print(result[0])
