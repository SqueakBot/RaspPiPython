# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import requests
import time

ipStr = '172.16.14.40:3000'
username = 'monkey'
pasword = '$2b$10$Bd4j22ohM..hAjYsqEuazu3eKkpYAlH6SHFCft/639U2cOU7RBZMG'
token = None

#Uncomment this to run normal
"""
print('made it here')
#import pdb;pdb.set_trace()
token_response = requests.post('http://'+ipStr+'/signin', data={'username':username, 'password': pasword}, timeout=5)
print(token_response.request)
"""

#This wchile attempt to connect every 5 seconds, comment out to run normal

token = requests.post('http://'+ipStr+'/signin',
                      headers={u'Authorization':u'Basic bW9ua2V5OmJhbmFuYQ=='},
                      data={'username':username, 'password': pasword})
response = requests.get('http://' + ipStr +'/questions/challenges',
                        headers={"Authorization": 'Bearer ' + token._content.decode()})

print(response._content.decode())




    
    

"""
response = requests.get('http://172.16.14.24:3000/questions/challenges')
print(response.json())

jsonResponse = response.json()
print(jsonResponse)

def getNewQuestion():
    tmp = requests.get('http://172.16.14.24:3000/questions/challenges')
    return tmp.json()

print(getNewQuestion())
"""
