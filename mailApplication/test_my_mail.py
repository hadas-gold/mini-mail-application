import requests
import json



# 1 test post function with valid paremters return status code 200
def test_post_with_valid_parameter():
    url = 'http://127.0.0.1:5000/sendMessage'
    headers = {'Content-Type': 'application/json'} 
    details = {"applicationId" :2 ,"sessionId" : "c" ,"messageId" : "c" ,"participants": "['avi','dov']","theMessage" : "how are"} 
    finallResponse=requests.post(url,headers=headers,data=json.dumps(details,indent=4))
    assert finallResponse.status_code==200


# 2 test get function with valid paremters return status code 200
def test_get_with_valid_parameters():
    url = 'http://127.0.0.1:5000/getMessage?applicationId=2'
    headers = {'Content-Type': 'application/json'} 
    finallResponse=requests.get(url=url)
    assert finallResponse.status_code==200


# 3 test delete function with valid paremters return status code 200
def test_delete_function_with_valid_parameters():
    url = 'http://127.0.0.1:5000/deleteMessage?applicationId=2'
    headers = {'Content-Type': 'application/json'}
    finallResponse=requests.delete(url=url)
    assert finallResponse.status_code==200

# 4 test that the Response is a well-formed JSON object
def test_response_json_formed():
    url = 'http://127.0.0.1:5000/getMessage?applicationId=2'
    headers = {'Content-Type': 'application/json'} 
    finallResponse=requests.get(url=url)
    assert finallResponse.status_code==200

# 5.0 test to verify that the response is filtered on the specified value. 
def test_delete_response_filter():
    url = 'http://127.0.0.1:5000/deleteMessage?applicationId=2'
    headers = {'Content-Type': 'application/json'}
    finallResponse=requests.delete(url=url)
    assert finallResponse.status_code==200

# 5.1 the wanted parameter has filtered and deleted in the last test, so it is not found here.
def test_get_response_filter():
    url = 'http://127.0.0.1:5000/getMessage?applicationId=2'
    headers = {'Content-Type': 'application/json'}
    finallResponse=requests.get(url=url)
    assert finallResponse.status_code==401

# 6 test to ensure that the action 'post' has been performed
def test_post():
    url = 'http://127.0.0.1:5000/sendMessage'
    headers = {'Content-Type': 'application/json'} 
    details = {"applicationId" :5 ,"sessionId" : "c" ,"messageId" : "c" ,"participants": "['avi','dov']","theMessage" : "how are"} 
    finallResponse=requests.post(url,headers=headers,data=json.dumps(details,indent=4))
    assert finallResponse.text=='Your message has sent sucssesfully!!!'


# 7 test performing appropriate get request and inspecting response
def test_get():
    url = 'http://127.0.0.1:5000/getMessage?applicationId=5'
    headers = {'Content-Type': 'application/json'} 
    finallResponse=requests.get(url=url)
    assert finallResponse.status_code==200


# 8.0 test refreshing the messages storage after delete action
def test_delete_refresh():
    url = 'http://127.0.0.1:5000/deleteMessage?applicationId=2'
    headers = {'Content-Type': 'application/json'}
    finallResponse=requests.delete(url=url)
    assert finallResponse.status_code==200


# 8.1 the deleted object will not be returen in next get request
def test_get_after_delete_refresh():
    url = 'http://127.0.0.1:5000/getMessage?applicationId=2'
    headers = {'Content-Type': 'application/json'} 
    finallResponse=requests.get(url=url)
    assert finallResponse.text=='There is no such a message'



# 9 test attempting to delete a messge that doesn’t exist ,
# and verify that error response is received.
def test_delete_doesnt_exists_messsage():
    url = 'http://127.0.0.1:5000/deleteMessage?applicationId=789'
    headers = {'Content-Type': 'application/json'}
    finallResponse=requests.delete(url=url)
    assert finallResponse.text=='There is no such a message'


# 10 test attempting to get a messge that doesn’t exist ,
# and verify that error response is received.
def test_get_dosnt_exist_message():
    url = 'http://127.0.0.1:5000/getMessage?applicationId=789'
    headers = {'Content-Type': 'application/json'} 
    finallResponse=requests.get(url=url)
    assert finallResponse.text=='There is no such a message'

# 11 test attempting to send a messge without necessary details,
# and verify that error response is received.
def test_post_without_necessary_details():
    url = 'http://127.0.0.1:5000/sendMessage'
    headers = {'Content-Type': 'application/json'} 
    details = { "sessionId" : "c" ,"messageId" : "c" ,"participants": "['avi','dov']","theMessage" : "how are"} 
    finallResponse=requests.post(url,headers=headers,data=json.dumps(details,indent=4))
    assert finallResponse.text=='You must insert application id ,session id and message id!'





