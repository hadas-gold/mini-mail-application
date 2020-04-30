import sqlite3
from flask import g
import requests
#conn=conToDB
#c=cur
#message = storageMessages
#messages=myMessage

conToDB=sqlite3.connect('storageMessages.db',check_same_thread=False)
cur= conToDB.cursor()

def create_db():
    cur= conToDB.cursor()
    cur.execute('CREATE TABLE IF NOT EXISTS myMessages (applicationId integer,sessionId TEXT,messageId TEXT,participants TEXT, content TEXT)')
    conToDB.commit()


def insert_to_sqlite(AppId,SessId,MessId,Part,TheMessage):
    cur.execute('INSERT INTO myMessages (applicationId ,sessionId ,messageId ,participants , content) VALUES(?,?,?,?,?) ',(AppId,SessId,MessId,Part,TheMessage))
    conToDB.commit()


def get_from_sqlite(title,request):
    cur.execute("SELECT * FROM myMessages WHERE "+title+"=?",([request]))
    dataToGet=cur.fetchall()
    return dataToGet


def delete_from_sqlite(Title,Request):
    checkData=get_from_sqlite(Title,Request)   
    if not checkData: 
        return False
    else:                 
        cur.execute("DELETE FROM myMessages WHERE "+Title+"=?",([Request]))
        conToDB.commit()
        return True


