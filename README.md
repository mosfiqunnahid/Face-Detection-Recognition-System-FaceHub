# Face-Detection-Recognition-System-FaceHub

# Introduction 
TODO: Biometrics is used in a facial recognition (face hub) device to map facial features from an image or video. To find a match, it compares the details to a database of recognized faces. This is due to the fact that facial recognition has a wide variety of commercial applications. It can be used for a variety of purposes, including surveillance and marketing. 

# Getting Started
TODO:- We need to follow this process. FaceDetection.py file detect the face. Then GenerateDataset.py require information to save sqlite database and collect 20 image in locally. TrainDataset convert all the image to data and create train.yml file. Which file is require for FaceRecognition.py file. Finaly FaceRecognition.py file show all the data about user and Recognize the user.
- FaceDetection.py - Detect Face
- GenerateDataset.py - Collect image + information
- TrainDataset.py - Create train.yml
- FaceRecognition.py - Final Result (Recognition)

1.	Installation process

To create a complete project on Face Recognition, we must work on 4 very distinct phases:
* Face Detection 
* Data Gathering
* Train the Recognizer
* Face Recognition

2.	Software dependencies

Python ^3.7.9  
pip 20.1.1  
Pillow 8.1.1  
dlib 19.21.1  
numpy 1.19.5  
tensorflow 2.4.1  
face-recognition 1.3.0  
opencv-python 4.5.1.48  
opencv-contrib-python 4.5.1.48  

also need to setup visual studio code c++ environment.

3.	Latest releases
4.	API references

# Build and Test
TODO:  We need to follow this process. FaceDetection.py file detect the face. Then GenerateDataset.py require information to save sqlite database and collect 20 image in locally. TrainDataset convert all the image to data and create train.yml file. Which file is require for FaceRecognition.py file. Finaly FaceRecognition.py file show all the data about user and Recognize the user.
- FaceDetection.py - Detect Face
- GenerateDataset.py - Collect image + information
- TrainDataset.py - Create train.yml
- FaceRecognition.py - Final Result (Recognition)

After clone this files need to create Classifiers folder with haarcasecade...xml files, dataSet, trainner folder.

# Contribute
LODO: We're using the encoder and the Haar Cascade classifier from opencv. So, if anyone uses the Machine Learning model and trains the dataset, the accuracy would improve. However, this type of approach necessitates the use of the cloud or a particular device to implement.

