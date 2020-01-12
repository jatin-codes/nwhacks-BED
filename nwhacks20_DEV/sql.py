import mysql.connector

class SQL:

    def __init__(self):
        self.db = mysql.connector.connect(user="linkr@nwhacks2020",
                                          password='Root.123',
                                          host="nwhacks2020.mysql.database.azure.com",
                                          port=3306,
                                          database='facial_rec')
        self.cursor = self.db.cursor()

    '''
    return a list of tuple (name, face_id) from database
    '''
    def get_face_ids(self):
        self.cursor.execute('SELECT name, face_id FROM users')
        result = self.cursor.fetchall()
        return result

    '''
    return a list of tuple (name, face_id) from database
    '''
    def get_friends(self, face_id):
        sql_command = 'SELECT name, face_id FROM users WHERE friend_id = ' + face_id
        self.cursor.execute(sql_command)
        result = self.cursor.fetchall()
        return result

    '''
    add a record to the table if the user friends with another user
    '''
    def insert_friend_record(self, name, friend_id):
        sql_command = 'INSERT INTO users (name, friend_id) VALUES (%s, %s)'
        val = (name, friend_id)
        self.cursor.execute(sql_command, val)
        self.db.commit()

    '''
    add a record to the table if new user sign up
    '''
    def insert_new_user(self, name, face_id):
        sql_command = 'INSERT INTO users (name, face_id) VALUES (%s, %s)'
        val = (name, face_id)
        self.cursor.execute(sql_command, val)
        self.db.commit()

    '''
    return the name of the user with this face id
    '''
    def get_name_from_fid(self, face_id):
        sql_command = 'SELECT name FROM users WHERE face_id = ' + face_id
        self.cursor.execute(sql_command)
        result = self.cursor.fetchone()
        return result