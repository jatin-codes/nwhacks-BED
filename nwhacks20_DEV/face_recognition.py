import asyncio
import io
import glob
import os
import sys
import time
import uuid
import requests
from urllib.parse import urlparse
from io import BytesIO
from PIL import Image, ImageDraw
from azure.cognitiveservices.vision.face import FaceClient
from msrest.authentication import CognitiveServicesCredentials
from azure.cognitiveservices.vision.face.models import TrainingStatusType, Person, SnapshotObjectType, OperationStatusType


#FACE_SUBSCRIPTION_KEY
KEY = '712e44c4280a4b31bb2bd34982673e97'

# FACE_ENDPOINT
ENDPOINT = 'https://thesocialmedia.cognitiveservices.azure.com/'

class FaceRecognition:

    def __init__(self):
        # Create an authenticated FaceClient.
        self.client = FaceClient(ENDPOINT, CognitiveServicesCredentials(KEY))

    '''
    return a list of  detected faces' ids (list[String])
    param: url (str) 
    '''
    def detect_faces(self, image_url):
        image_name = os.path.basename(image_url)
        detected_faces = self.client.face.detect_with_url(url=image_url)

        if not detected_faces:
            raise Exception('No face detected from image {}'.format(image_name))
        '''
        print('Detected faces from', image_name, ':')
        for face in detected_faces:
            print(face.face_id)
        '''

        detected_face_ids = list(map(lambda x: x.face_id, detected_faces))

        return detected_face_ids


    '''
    return if the user_face_id is among the face_ids from detected_faces
    param: user_face_id (str), list[DetectedFace] (DetectedFace class)
    '''
    def detect_similar_faces(self, face_id, detected_face_ids):
        similar_faces = self.client.face.find_similar(face_id=face_id, face_ids=detected_face_ids)
        if not similar_faces[0]:
            return False
        else:
            return True
