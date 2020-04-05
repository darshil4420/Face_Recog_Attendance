"""-----------------------------------------
step 4：
    Turn on the camera to recognize the face；
-----------------------------------------"""
# -*- coding:utf-8 -*-
import cv2
from train_model import Model
from load_dataset import read_name_list
import time,os
from datetime import datetime
class Camera_reader(object):
    # Build the model when initializing the camera and load the trained model
    def __init__(self):
        self.model = Model()
        self.model.load()
        self.img_size = 128

    def build_camera(self):
        # The location of the face cascade file in the opencv file, used to help identify faces in images or video streams
        face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_alt.xml')
        # Read the subfolder name under the dataset
        name_list = read_name_list('./dataset')

        # Turn on the camera and start reading
        cameraCapture = cv2.VideoCapture(700)
        success, frame = cameraCapture.read()

        while success and cv2.waitKey(1) == -1:
            success, frame = cameraCapture.read()
            # Grayscale image
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            # Face detection: scaleFactor is
            #the magnification ratio (this parameter must be greater than 1);
            #minNeighbors is the number of repeated identifications (this parameter is used to adjust the accuracy, the larger the more accurate)
            faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=8)
            for (x, y, w, h) in faces:
                origin = gray[x:x + w, y:y + h]
                # origin is the original image, self.img_size is the size of the output image, and interpolation is the interpolation method
                origin = cv2.resize(origin, (self.img_size, self.img_size), interpolation=cv2.INTER_LINEAR)
                # Use the model to compare the faces recognized by cv2
                label, prob = self.model.predict(origin)
                # If the model believes that the probability is higher than 70%, it will be displayed as the existing label in the model
                if prob > 0.7:
                    show_name = name_list[label]
                        
                    
                    
                else:
                    show_name = 'unknown'

                # Frame a face
                
                frame = cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 1)
                if prob > 0.7:
                    #storing recognized folder in folder named with date of that day
                    today = datetime.now()
                    recpath='./Recognized/'+today.strftime("%d-%m-%Y")
                    if not os.path.exists(recpath):
                        os.makedirs(recpath)
                        #print(os.getcwd())
                    cv2.imwrite(recpath+'/'+today.strftime("%H%M%S")+'.jpg',frame[y:y + h, x:x + w])
                    #if not os.path.exists()
                
                # Show name
                cv2.putText(frame, show_name, (x, y - 20), cv2.FONT_HERSHEY_SIMPLEX, 1, 255, 2)

            cv2.imshow("Recognizing...", frame)
        # Release camera
        cameraCapture.release()
        # Close all windows
        cv2.destroyAllWindows()


if __name__ == '__main__':
    camera = Camera_reader()
    camera.build_camera()
