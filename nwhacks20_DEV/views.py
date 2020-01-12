from django.http import HttpResponse
import json
# from nwhacks20_DEV.sql import SQL

from nwhacks20_DEV.face_recognition import FaceRecognition
# from face_recognition import FaceRecognition

CORA_FACE_ID = 'f2abd556-72f7-4826-a2b6-c9e5837e230212:29'
HUY_FACE_ID = 'e440a597-7c01-424f-b8d0-a42501fe3ee8'

face_reg = FaceRecognition()

def get_user(request):
    face_ids_from_img = face_reg.detect_faces('https://firebasestorage.googleapis.com/v0/b/nwhacks20-56ead.appspot.com/o/images%2Fstrict%2Fgroup-photo%20(1).jpg?alt=media&token=d89f5c21-4ea6-49bd-a925-085548ac5282')
    cora_face_id = face_reg.detect_faces('https://firebasestorage.googleapis.com/v0/b/nwhacks20-56ead.appspot.com/o/images%2Fstrict%2Fcora.jpg?alt=media&token=fb214178-5854-4d01-9a2e-2bfeab007250')
    huy_face_id = face_reg.detect_faces('https://firebasestorage.googleapis.com/v0/b/nwhacks20-56ead.appspot.com/o/images%2Fstrict%2Fhuy%20(5).jpg?alt=media&token=73f27610-ba15-455e-ab02-8de84e7dd464')
    cora_id = cora_face_id[0]
    huy_id = huy_face_id[0]
    if face_reg.detect_similar_faces(cora_id, face_ids_from_img):
        if face_reg.detect_similar_faces(huy_id, face_ids_from_img):
            return HttpResponse(huy_id)

    return HttpResponse('NONE')
    
