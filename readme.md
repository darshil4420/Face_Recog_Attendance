
Note:

The dataset folder is the data set;

MyModel folder stores the asking price of the trained model;

The model_test folder is used to store the photos and videos to be tested when testing the model;

The my_faces and MySource_faces folders are used to test the collection of face data sets.

****************************

One: collect face data set
From photo collection: faces_from_Photo.py
Capture from video file: faces_from_Video.py
Collected from the camera: faces_from_Camera.py

Function to load photos: read_img.py


Two: process photos and load tags
load_dataset.py

Three: build and train the model
train_model.py

Functions for processing data sets: dataSet.py

Four: model testing
Recognize faces in photos: Recognize_From_Photo.py
Recognize faces in video files: Recognize_From_Vedio.py
Identify the face in the camera: Recognize_From_Camera.py
