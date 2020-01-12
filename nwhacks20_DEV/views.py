from django.http import HttpResponse
import json
from nwhacks20_DEV.sql import SQL
from nwhacks20_DEV.face_recognition import FaceRecognition

face_reg = FaceRecognition()
sql = SQL()

'''
def store_images(request):
    return HttpResponse('YESSSS')


def detect_faces(request, img_url):
    return face_reg.detect_faces(img_url)


def detect_similar_face(request, face_id, dectected_face_ids):
    return face_reg.detect_similar_faces(face_id, dectected_face_ids)
'''


def add_friends(request):
    data = json.loads(request.body)
    img_url = data.get('image_url')

    face_ids_from_img = face_reg.detect_faces(img_url)
    face_ids_from_db = sql.get_face_ids()
    face_ids = []
    for id_from_db in face_ids_from_db:
        if face_reg.detect_similar_faces(id_from_db, face_ids_from_img):
            face_ids.append(id_from_db)
    names = []
    for face_id in face_ids:
        name = sql.get_name_from_fid(face_id)
        names.append(name)
    names.reverse()
    for (name, face_id) in zip(names, face_ids):
        sql.insert_friend_record(name, face_id)
    return HttpResponse('')






'''
def get_face_ids_from_db(request):
    return sql.get_face_ids()

def get_friends_from_db(request):
    return sql.get_friends()

def push_friend_record_to_db(request):
    return sql.insert_friend_record()

def push_new_user_to_db(request):
    return sql.insert_new_user()
'''