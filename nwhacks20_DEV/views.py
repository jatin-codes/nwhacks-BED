from django.http import HttpResponse
import json
from nwhacks20_DEV.sql import SQL
from nwhacks20_DEV.face_recognition import FaceRecognition

face_reg = FaceRecognition()
sql = SQL()

'''
def get_user(request):
    face_ids_from_img = face_reg.detect_faces('https://firebasestorage.googleapis.com/v0/b/nwhacks20-56ead.appspot.com/o/images%2Fstrict%2Fgroup-photo%20(1).jpg?alt=media&token=d89f5c21-4ea6-49bd-a925-085548ac5282')
    cora_face_id = face_reg.detect_faces('https://firebasestorage.googleapis.com/v0/b/nwhacks20-56ead.appspot.com/o/images%2Fstrict%2Fcora.jpg?alt=media&token=fb214178-5854-4d01-9a2e-2bfeab007250')
    huy_face_id = face_reg.detect_faces('https://firebasestorage.googleapis.com/v0/b/nwhacks20-56ead.appspot.com/o/images%2Fstrict%2Fhuy%20(5).jpg?alt=media&token=73f27610-ba15-455e-ab02-8de84e7dd464')
    cora_id = cora_face_id[0]
    huy_id = huy_face_id[0]
    if face_reg.detect_similar_faces(cora_id, face_ids_from_img):
        if face_reg.detect_similar_faces(huy_id, face_ids_from_img):
            return HttpResponse('Huy is in there')
    return HttpResponse('NONE')
'''

# what happen if user take a picture
def request_response_camera(request):
    img_url = 'fixed designated url for an img taken from ap'
    face_ids_from_img = face_reg.detect_faces(img_url)
    face_ids_from_db = sql.get_face_ids()

    # check initial requirement for human in pictures
    if len(face_ids_from_img) == 0:
        return HttpResponse('no faces in img')
    elif len(face_ids_from_img) == 1:
        return HttpResponse('not enough faces in img')

    # check if user is in the picture
    for id_from_img in face_ids_from_img:
        if face_reg.detect_similar_faces(id_from_img, '*user face_id*'):
            face_ids_from_img.remove(id_from_img)
        else:
            return HttpResponse('could not find user in img')

    # the next step is brute force due to hackathon's time limitation
    # find non-user humans and look up in db to check if there's a matching profile
    for id_from_img in face_ids_from_img:
        for id_from_db in face_ids_from_db:
            if face_reg.detect_similar_faces(id_from_img, id_from_db):
                sql.insert_friend_record('*user name*', id_from_db)
    return HttpResponse('The function should not reach here')  # ugly coding

# return what to show on newsfeed on chronological order
# to be implemented
def request_response_home():
    return HttpResponse('')
