from django.http import HttpResponse
import json
from nwhacks20_DEV.sql import SQL
from nwhacks20_DEV.face_recognition import FaceRecognition

face_reg = FaceRecognition()
sql = SQL()


def store_images(request):
    return HttpResponse('YESSSS')

'''
def detect_faces(request, img_url):
    return face_reg.detect_faces(img_url)


def detect_similar_face(request, face_id, dectected_face_ids):
    return face_reg.detect_similar_faces(face_id, dectected_face_ids)
'''


def add_friends(request):
    img_url = 'https://lh3.googleusercontent.com/EQS5SSPak-cL_eNz0nyUPn_HLyHabOwx4X9xRUkDxBuqAYxpVmr53ul68Ekyhz6NFWPMOVKvv4bGo3pCvzIiWEvywCm_kJxWSFhC2Dg7CJBBsUjHLBr1pZa4UcAhBmJLoysJx3WDutv4k3QnGTqoBLRbJREeIC3o6BY1rNFcVcvbJVtiwnpilGpF5CJsUN6Og6qp2QWX9AZ9YNwbEYITQL7jylLHvhGtPj_2_yoV3uBKvne-tZ67EQnwI-O985QDrtXxIPAQ_wGZev0NwUp89q545G_9ojp0HVedCzDeODTyGbisN7C15cAracEP0yJyt7EPhl0Ab7EWB-lQWtYE_3SEzKVG9L5fd0BEjU25qkVN6yh8MbmcaNNtGEADoxrMbkZiN86ZNA4w26iiWmfASDxvU3j9H6UYAsppeKujCTJBcAUJh6JpvQeAAvKcDJy2d_neFFgz7cJOypYjocla2sGv8-ts9zDqMge-ihZxuyz5OGC6olbaTSD71CbMzIxizerAfnYbkntjNsaHGE5s9dqf55oxc7duCZSG7S9XQfN0gLLEZdukzYnkYjDAzcUYyD8iBUdn01tFMZGbVwOFDxZ81E6LoeM0SLO33a8Y4dXGAiSGBHSEPRPbOVzYhxDWhzEpoUN8rLAplI76_eH8ZwkvmVruT2RseOBleEplgeIm7Tl2aWbgYao=w1428-h1903-no'

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

def get_user(request):
    img_url = 'https://lh3.googleusercontent.com/EQS5SSPak-cL_eNz0nyUPn_HLyHabOwx4X9xRUkDxBuqAYxpVmr53ul68Ekyhz6NFWPMOVKvv4bGo3pCvzIiWEvywCm_kJxWSFhC2Dg7CJBBsUjHLBr1pZa4UcAhBmJLoysJx3WDutv4k3QnGTqoBLRbJREeIC3o6BY1rNFcVcvbJVtiwnpilGpF5CJsUN6Og6qp2QWX9AZ9YNwbEYITQL7jylLHvhGtPj_2_yoV3uBKvne-tZ67EQnwI-O985QDrtXxIPAQ_wGZev0NwUp89q545G_9ojp0HVedCzDeODTyGbisN7C15cAracEP0yJyt7EPhl0Ab7EWB-lQWtYE_3SEzKVG9L5fd0BEjU25qkVN6yh8MbmcaNNtGEADoxrMbkZiN86ZNA4w26iiWmfASDxvU3j9H6UYAsppeKujCTJBcAUJh6JpvQeAAvKcDJy2d_neFFgz7cJOypYjocla2sGv8-ts9zDqMge-ihZxuyz5OGC6olbaTSD71CbMzIxizerAfnYbkntjNsaHGE5s9dqf55oxc7duCZSG7S9XQfN0gLLEZdukzYnkYjDAzcUYyD8iBUdn01tFMZGbVwOFDxZ81E6LoeM0SLO33a8Y4dXGAiSGBHSEPRPbOVzYhxDWhzEpoUN8rLAplI76_eH8ZwkvmVruT2RseOBleEplgeIm7Tl2aWbgYao=w1428-h1903-no'
    face_ids = face_reg.detect_faces(img_url)
    for face_id in face_ids:
        name = sql.get_name_from_fid(face_id)
        if not (name == 'Cora'):
            return HttpResponse({
                'name' : name
            })

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