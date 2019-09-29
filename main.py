from flask import Flask, request, render_template
import urllib
from datetime import datetime
import calendar
import time
import json
import os
import numpy as np
import cv2
import mysql.connector
from mysql.connector import Error
from face_search_api import face_search_api as faceSearch
from datapopulator import datapopulator as dataPopulator 
from werkzeug import secure_filename
from shutil import copyfile
pwd = os.getcwd()
app = Flask(__name__)
path = ""
ts = ""
src = ""
dp=dataPopulator()
try:
    connection = mysql.connector.connect(host='localhost',
                                         database='hackuta',
                                         user='root',
                                         password='root')

    if connection.is_connected():
        db_Info = connection.get_server_info()
        print("Connected to MySQL Server version ", db_Info)
        cursor = connection.cursor()
        cursor.execute("select database();")
        record = cursor.fetchone()
        print("Your connected to database: ", record)

except Error as e:
    print("Error while connecting to MySQL", e)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/takePic/', methods = ['GET'])
def takePic():
    global path
    global ts
    global src
    global connection
    cap = cv2.VideoCapture(0) # video capture source camera (Here webcam of laptop) 
    ret,frame = cap.read() # return a single frame in variable `frame`
    ts = calendar.timegm(time.gmtime())
    print(ts)
    path = pwd+r"/static/images/"+str(ts)+".png"
    print(path)
    while(True):
        cv2.imshow('img1',frame) #display the captured image
        #if cv2.waitKey(1) & 0xFF == ord('y'): #save on pressing 'y'
            
        cv2.imwrite(path,frame)
        cv2.destroyAllWindows()
        break
    
    cap.release()
    src=r"/static/images/"+str(ts)+".png"
    query = "INSERT INTO new_img (test_path) VALUES(\""+str(ts)+".png\")"
    print(query)
    cursor = connection.cursor()
    cursor.execute(query)
    connection.commit()
    
    return render_template('displayPic.html', newpath=src)

@app.route('/uploader', methods = ['GET', 'POST'])
def upload_file():
    global path
    global src
    if request.method == 'POST':
        f = request.files['file']
        filename=f.filename
        uploaddst = os.getcwd()+r"/static/images/"+str(f.filename)
        f.save(secure_filename(f.filename))
        uploadsrc=os.getcwd()+"//"+str(f.filename)
        copyfile(uploadsrc, uploaddst)
        newsrc=r"/static/images/"+filename
        src = newsrc
    path = os.getcwd()+r"/static/images/"+str(f.filename)
    return render_template('displayPic.html', newpath=newsrc)

@app.route('/showResults/', methods = ['GET'])
def showResults():
    global path
    global src
    ids= []
    result = []
    print("path in search results: ")
    print(path)
    fs = faceSearch(path)
    ids = fs.compare_faces()
    print(ids)
    connection = mysql.connector.connect(host='localhost',
                                         database='hackuta',
                                         user='root',
                                         password='root')
    for i in ids:
        query = "SELECT * FROM hackuta.user_data where id ="+str(i)+";"
        cursor = connection.cursor()
        cursor.execute(query)
        records = cursor.fetchall()
        for row in records:
            newsrc=r"/static/images/"+row[1]
            result.append(newsrc)
    
    print(result)
    print(ids)
    return render_template('showResults.html', newpath=src, len=len(result), res=result, idArray=ids)

#@app.route('/showroomfinal/<int:room>/<int:roomend>')
@app.route('/showTransaction/<int:profId>')
def showTransaction(profId=None):
    global path
    global src
    print("Inside showtransaction")
    print(profId)
    res1, res2 = dp.findIDDetails(profId)
    print (res1)
    print(res2)
    query = "SELECT * FROM hackuta.user_data where id ="+str(profId)+";"
    print(query)
    cursor = connection.cursor()
    cursor.execute(query)
    records = cursor.fetchall()
    for row in records:
        newsrc=r"/static/images/"+row[1]
        
    print(newsrc)
        
    return render_template('showTransaction.html', resname=res1, restrans=res2, src=src, newsrc=newsrc)
	
	

		
#to pass a variable use <>
#to specify the datatype: <int:postid>
#datatype not required for string
'''
@app.route('/profile/<username>')
def profile(username):
	return render_template("profile.html", name = username)
	
#to show different kind of request methods
#to specify that this page can receive data through both GET and Post
@app.route('/bacon', methods=['GET','POST'])
def bacon():
	if request.method == 'POST':
		return "this is using POST"
	else:
		return "this is GET"

@app.route('/salary/')
def salary():
	
	sql = 'Select "Studentname" from HMZ29592.PEOPLEINFO where "Grade" > 85;'
	stmt = ibm_db.prepare(connection,sql)
	ibm_db.execute(stmt)
	rows=[]
	result = ibm_db.fetch_assoc(stmt)
	while result != False:
		rows.append(result.copy())
		result = ibm_db.fetch_assoc(stmt)
	# close database connection
	ibm_db.close(connection)
	return render_template('salary.html', ci=rows)

@app.route('/update/<int:marks>')
def update(marks=None):
	
	sql = 'UPDATE HMZ29592.PEOPLEINFO set "Grade" = '+str(marks)+' where "Studentname" = \'Sue\';'
	stmt = ibm_db.prepare(connection,sql)
	if ibm_db.execute(stmt):
		return render_template('update.html')
	# close database connection
	ibm_db.close(connection)
	
	
@app.route('/showroom/')
def showroom():
	return render_template('showroom.html')
	
@app.route('/showroomfinal/<int:room>/<int:roomend>')
def showroomfinal(room=None, roomend = None):
	sql = 'Select "Name", "City", "Room"  from HMZ29592.PEOPLE where "Room" > '+str(room)+' and "Room" < '+str(roomend)+';'
	print sql;
	stmt = ibm_db.prepare(connection,sql)
	ibm_db.execute(stmt)
	rows=[]
	result = ibm_db.fetch_assoc(stmt)
	while result != False:
		rows.append(result.copy())
		result = ibm_db.fetch_assoc(stmt)
	# close database connection
	ibm_db.close(connection)
	return render_template('showroomfinal.html', ci=rows)
	
	
'''	
	
	
if __name__ == '__main__':
	#app.run(host ='0.0.0.0', port = port, debug = True)
	app.run(debug = True)
 