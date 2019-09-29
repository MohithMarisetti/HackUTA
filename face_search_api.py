#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 28 14:23:12 2019

@author: harshitshah
"""

import face_recognition 
import cv2
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import mysql.connector
from mysql.connector import Error
import os


class face_search_api:
    imgPath = os.getcwd() + r"/static/images/"
    def __init__(self,test):
        print("inside face search")
        print(test)
        self.test = test
        
        try:
            
            self.connection = mysql.connector.connect(host='localhost',
                                         database='hackuta',
                                         user='root',
                                         password='root')

            if self.connection.is_connected():
                db_Info = self.connection.get_server_info()
                print("Connected to MySQL Server version ", db_Info)
                cursor = self.connection.cursor()
                cursor.execute("select database();")
                record = cursor.fetchone()
                print("Your connected to database: ", record)

        except Error as e:
            print("Error while connecting to MySQL", e)
        
    
    
    def compare_faces(self):
        new_best_match_index=[]
        known_face_encodings,known_face_names = [],[]
        sql_select_Query = "SELECT * FROM user_data"
        cursor = self.connection.cursor()
        cursor.execute(sql_select_Query)
        records = cursor.fetchall()
        for row in records:
            uid = row[0]
            imgPath = os.getcwd() + r"/static/images/"
            path = row[1]
            image = face_recognition.load_image_file(imgPath+path)
            print("Image file*************")
            
            vector = face_recognition.face_encodings(image)[0]
            print(vector)
            known_face_names.append(uid)
            known_face_encodings.append(vector)
            print("Inside Harshits code")
            print(known_face_names)
        if (self.connection.is_connected()):
            cursor.close()
            self.connection.close()
            print("MySQL connection is closed")
           
        image = face_recognition.load_image_file(self.test)
        test_face_encoding = face_recognition.face_encodings(image)[0]
        matches = face_recognition.compare_faces(known_face_encodings, test_face_encoding)
        face_distances = face_recognition.face_distance(known_face_encodings, test_face_encoding)
        best_match_index = np.argsort(face_distances)
        print(best_match_index)
        for i in best_match_index:
            new_best_match_index.append(known_face_names[i])

            
        return new_best_match_index
            
        
    def insert_data(self):
        image = face_recognition.load_image_file(self.test)
        vector = face_recognition.face_encodings(image)[0]
        query = "INSERT INTO user_data(path,vector) VALUES(%s,%s)"
        args = (path,vector.dumps(),)
        cursor = self.connection.cursor()
        cursor.execute(query,args)
        if cursor.lastrowid:
            print('last insert id', cursor.lastrowid)
        else:
            print('last insert id not found')
 
        self.connection.commit()
        if (self.connection.is_connected()):
            cursor.close()
            self.connection.close()
            print("MySQL connection is closed")
        
        
