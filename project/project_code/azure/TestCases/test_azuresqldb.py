import requests
import logging
import json
import jsonpath


def test_get_database():
   # url = 'http://0.0.0.0:8080/cloudmesh/v3/ui/#/Database%20Registry/cloudmesh.database.get'

    url =  'http://0.0.0.0:8080/cloudmesh/v3/database'
    response = requests.get(url)
    assert response.status_code == 200
    print(response.content)
'''
def test_create_new_database():
    file = open('create_database.json','r')
    json_input =file.read()
    request_json = json.loads(json_input)
    # put request with JSON input dfata
    response = requests.put(url, request_json)
    #validate response code
    assert response.status_code ==200
    print(response.header.get('Content-Length'))
    #parse response to Json format
    response_json = json.loads(response.text)
    #pick id uisng Json Path
    id = jsonpath.jsonpath(respone_json,'id')
    print(id[0])

'''
def test_get_schema():
    url =  'http://0.0.0.0:8080/cloudmesh/v3/database/absdb/schema/all'
    response = requests.get(url)
    assert response.status_code == 200
    print(response.content)

def test_put_schema():
    url =  'http://0.0.0.0:8080/cloudmesh/v3/database/testdb/schema/pycheck_sch'
   # file = open('create_database.json','r')
   # json_input =file.read()
   # request_json = json.loads(json_input)
    # put request with JSON input dfata
    response = requests.put(url)
    #validate response code
    assert response.status_code == 500
    #print(response.header.get('Content-Length'))
    #parse response to Json format
    #response_json = json.loads(response.text)
    #pick id uisng Json Path
    #id = jsonpath.jsonpath(respone_json,'id')
    #print(id[0])