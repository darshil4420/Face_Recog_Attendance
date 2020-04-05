"""-----------------------------------------
step 1: Load face data from photos;
         One label at a time;
         Load all photos in the changed path from the source folder and store them in the target path,
     The name of the destination path folder is the label for the batch of photos;
----------------------------------------- """
# -*-coding:utf8-*-
import os
import cv2
import time
from read_img import readAllImg

"""
Read all photos from the source path and put them in a list, then check them one by one, buckle the faces in them, and store them in the target path
"""
# sourcePath is the folder to store the image source, objectPath is the folder to store the recognized face, * suffix is the format of the source file
def readPicSaveFace(sourcePath, objectPath, *suffix):
    try:
        # Read the photo, note that the first element is the file name
        resultArray = readAllImg(sourcePath, *suffix)

        # Check the pictures in the list one by one, find the faces in them and write them to the target folder
        count = 1
        # Load face feature library
        face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_alt.xml')
        for i in resultArray:
            if type(i) != str:
                gray = cv2.cvtColor(i, cv2.COLOR_BGR2GRAY)
                faces = face_cascade.detectMultiScale(gray, 1.3, 5)
                for (x, y, w, h) in faces:
                    # File name with timestamp and reading order
                    listStr = [str(int(time.time())), str(count)]
                    print(listStr)
                    fileName = ''.join(listStr)

                    f = cv2.resize(gray[y:(y + h), x:(x + w)], (200, 200))
                    cv2.imwrite(objectPath + os.sep + '%s.jpg' % fileName, f)
                    count += 1

    except IOError:
        print("Error")

    else:
        print('Already read ' + str(count - 1) + ' Photos to ' + objectPath + 'directory')



if __name__ == '__main__':
    """
    第一个参数：是存储源文件图片的文件夹地址；
    第二个参数：是存储剪裁好、处理好的人脸图片的地址；
    后面的图片格式：源文件图片的格式（文件后缀）。
    """
    # ./dataset/panwei
    readPicSaveFace('./MySource_faces', './my_faces', '.jpg', '.JPG', 'png', 'PNG')
