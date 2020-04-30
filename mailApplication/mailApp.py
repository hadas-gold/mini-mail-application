from flask import Flask, jsonify, request,Response
import json
import dbQuery
from dbQuery import *
myMail = Flask(__name__)


dbQuery.create_db()

@myMail.route('/sendMessage',methods=['post'])
def post():
    dataToPost=request.get_json()
    if 'applicationId' in dataToPost and 'sessionId' in dataToPost and 'messageId' in dataToPost:    
        appId = dataToPost['applicationId']
        sessId = dataToPost['sessionId']
        messId = dataToPost['messageId']
        part= dataToPost['participants']
        content = dataToPost['theMessage']
        dbQuery.insert_to_sqlite(appId,sessId,messId,part,content)
        return Response('Your message has sent sucssesfully!!!' ,status=200,mimetype='application/json')
    else:
        return Response('You must insert application id ,session id and message id!', status=400,mimetype='application/json')





@myMail.route('/getMessage', methods=['get'])
def get():

    responseList=None

    if 'applicationId' in request.args:
        responseList=dbQuery.get_from_sqlite('applicationId',request.args['applicationId'])

    elif 'sessionId' in request.args:
        responseList=dbQuery.get_from_sqlite('sessionId',request.args['sessionId'])

    elif 'messageId' in request.args:
        responseList=dbQuery.get_from_sqlite('messageId',request.args['messageId'])

    if responseList:
        jsonResponse=json.dumps(responseList,default=lambda x:x.__dict__)
        return Response(jsonResponse,status=200,mimetype='application/json')
    else:    
        return Response('There is no such a message',status=401,mimetype='application/json')



@myMail.route('/deleteMessage', methods=['delete'])
def delete():

    checkBool=None

    if 'applicationId' in request.args:
        checkBool=dbQuery.delete_from_sqlite('applicationId',request.args['applicationId'])

    elif 'sessionId' in request.args:
        checkBool=dbQuery.delete_from_sqlite('sessionId',request.args['sessionId'])

    elif 'messageId' in request.args:
        checkBool=dbQuery.delete_from_sqlite('messageId',request.args['messageId'])

    if checkBool==True:
        return Response('Your messages deleted sucssesfully!!!',status=200,mimetype='application/json')
    else:
        return Response('There is no such a message',status=401,mimetype='application/json')

myMail.run()


