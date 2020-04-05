"""-----------------------------------------
step 1: Collect face data from the camera;
         One label at a time;
         Get several pieces of my face data set, using dlib to
     Face recognition, although the speed is slower than OpenCV recognition, but the recognition effect
     Fruit is better.
         Face size: 128 * 128
----------------------------------------- """
import cv2
import dlib
import os
import random
name=input('What is Your Name?:')
# The more photos collected, the clearer the better
# Faces_my_path folder lowers its own avatar after detection
faces_my_path = './dataset/'+name
# Image size
size = 128
# If the directory does not exist, create the directory first
if not os.path.exists(faces_my_path):
    os.makedirs(faces_my_path)


"" "Change the relevant parameters of the picture: brightness and contrast" ""
def img_change(img, light=1, bias=0):
    width = img.shape[1]
    height = img.shape[0]
    for i in range(0, width):
        for j in range(0, height):
            for k in range(3):
                tmp = int(img[j, i, k] * light + bias)
                if tmp > 255:
                    tmp = 255
                elif tmp < 0:
                    tmp = 0
                img[j, i, k] = tmp
    return img


# Feature extractor: dlib comes with frontal_face_detector, which is the face detector
detector = dlib.get_frontal_face_detector()

#Create window
cv2.namedWindow('Collecting photos', 1)
# Resize the window
cv2.resizeWindow('Collecting photos', 400, 300)
# Turn on the camera; the built-in camera is 0, if there are other cameras, it is 1,2,3,4 ...
camera = cv2.VideoCapture(700)

if False == camera.isOpened():
    print("The camera could not be turned on.")
else:
    print("The camera is turned on!")

# counter
index = 1
# My face data set capacity
datasetSize = 200
while True:
    if (index <= datasetSize):
        success, img = camera.read()
        if success:
            print("The camera read the image successfully!", index)
        else:
            print("Failed to read the image through the camera!")

        # print("step1:", img)

        gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        # print("step2:", gray_img)
        #Face detection using detector
        dets = detector(gray_img, 1)
        """----------------------------------------------- ---------------------
         Use the enumerate function to traverse the elements and their subscripts in the sequence, i is the face number, and d is the element corresponding to i;
         left: the distance from the left side of the face to the left border of the picture; right: the distance from the right side of the face to the left border of the picture
         top: the distance from the top of the picture to the top of the picture; bottom: the distance from the bottom of the face to the top of the picture
         -------------------------------------------------- -------------------- """
        for i, d in enumerate(dets):
            x1 = d.top() if d.top() > 0 else 0
            y1 = d.bottom() if d.bottom() > 0 else 0
            x2 = d.left() if d.left() > 0 else 0
            y2 = d.right() if d.right() > 0 else 0

            face = img[x1:y1, x2:y2]
            """Adjust the brightness and contrast of the picture. 
            The brightness and contrast values are random numbers, which can increase the diversity of the sample."""
            face = img_change(face, random.uniform(0.5, 1.5), random.randint(-50, 50))

            face = cv2.resize(face, (size, size))

            cv2.imshow('image', face)

            cv2.imwrite(faces_my_path + '/' + str(index) + '.jpg', face)
            index += 1

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        print("mine", datasetSize, "The face image collection is completed.")
        break
