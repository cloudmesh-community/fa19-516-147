############################################################################
# database.py is to create database ,scheme ,table and query in Azure      #
# Section azuresqldb added in the file                                     #
############################################################################

import os
import subprocess
from cloudmesh.common.dotdict import dotdict
from cloudmesh.configuration.Config import Config
from flask import request, jsonify
from pymongo import MongoClient
import json


def status():
    d = {"status": "ok"}
    return jsonify(d)


############################################################################
# Read database connection detail from .cloudmesh/cloudmesh.yaml file      #
# Section azuresqldb added in the file                                     #
############################################################################

service_name = 'mongodb'
config = Config()
credential = dotdict(config[f"cloudmesh.database.{service_name}.credentials"])


'''
server = SSHTunnelForwarder(
    MONGO_HOST,
    ssh_username=MONGO_USER,
    ssh_password=MONGO_PASS,
    remote_bind_address=(MONGO_HOST, 27017)
)

server.start()

client = pymongo.MongoClient(MONGO_HOST, server.local_bind_port) # server.local_bind_port is assigned local port
db = client[MONGO_DB]
pprint.pprint(db.collection_names())

server.stop()
'''
server = credential.server
database = credential.database
username = credential.username
password = credential.password
driver = credential.driver
port = 1433


#########################################################################################
# Helper functions                                                     #
# get database list, connect , disconnect a database                                  #
#########################################################################################

def _connect():
    global MONGO_HOST
    client = MongoClient(MONGO_HOST, 27017)


#########################################################################################
# Function for database operations                                                      #
# get database list, connect , disconnect a database                                    #
#########################################################################################

def get(dbname):
    dbs = MongoClient(MONGO_HOST, 27017).list_database_names()
    return json.dumps(dbs)


def put(dbname):
    client = MongoClient(MONGO_HOST, 27017)
    dbname = str(dbname)
    db = client[dbname]


def delete(dbname):
    client = MongoClient(MONGO_HOST, 27017)
    dbname = str(dbname)
    db = client.drop_database(dbname)

def get_coll(dbname, collname):
    # con = _connect()
    client = MongoClient(MONGO_HOST, 27017)
    # coll_nm = db.getCollectionNames()
    db = client[dbname]
    coll_nm = db.list_collection_names()
    return json.dumps(coll_nm)


# ****** Function to create a collection in a database , database name is a input parameter for this function ******


def put_coll(dbname, collname):
    con = _connect()
    client = MongoClient(MONGO_HOST, 27017)
    # coll_nm = db.getCollectionNames()
    db = client[dbname]
    coll_nm = db[collname]

# ****** Function to delete collection from database *******

def delete_coll(dbname, collname):
    con = _connect()


# ******Function to get data from a database table ******

def data_get(dbname, collname):
    con = _connect()
    ftype = ".json"
    fname = collname+ftype
    command = f"mongoexport --host localhost:27017 --db {dbname} --collection {collname}  --out {fname}"
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, shell=True)
    #for data in process.stdout:
    #print data

# ******Function to load data into a database collection ******

def data_put(dbname, collname):
    con = _connect()
    client = MongoClient(MONGO_HOST, 27017)
    db = client[dbname]
    coll = db[collname]
    data_dict = request.json
    x = coll.insert_one(data_dict)
    key = list(data_dict.keys())
    key1 = str(key)
    key2 = key1.replace('[', '(')
    key3 = key2.replace(']', ')')
    key4 = key3.replace("'", "")
    val = list(data_dict.values())
    val1 = str(val)
    val2 = val1.replace('[', '(')
    val3 = val2.replace(']', ')')


def data_delete(dbname, collname):
    client = MongoClient(MONGO_HOST, 27017)
    query_param = request.args
    col1 = query_param.get('col1')
    val1 = query_param.get('val1')
    db = client[dbname]
    coll = db[collname]
    myquery = { col1 : val1 }
    r = coll.delete_many(myquery)
    return r.deleted_count


def index_put(dbname, collname, idxnm):
    con = _connect()
    client = MongoClient(MONGO_HOST, 27017)
    db = client[dbname]
    coll = db[collname]
    coll.create_index({idxnm : 1})

def index_get(dbname, collname, idxnm):
    client = MongoClient(MONGO_HOST, 27017)
    db = client[dbname]
    coll = db[collname]
    ind = coll.index_information()
    return json.dumps(ind)

def index_delete(dbname, collname, idxnm):
    client = MongoClient(MONGO_HOST, 27017)
    db = client[dbname]
    coll = db[collname]
    coll.drop_index(idxnm)

def index_patch(dbname, collname, idxnm):
    client = MongoClient(MONGO_HOST, 27017)
    db = client[dbname]
    coll = db[collname]
    coll.drop_index(idxnm)

def data_post(dbname, collname):
    con = _connect()
    data_dict = request.json
    fname = data_dict['FileName']
    ftype = data_dict['FileType']
    fpath = data_dict['FilePath']
    fmode = data_dict['FileMode']
    #command = f"mongoimport {auth} --bind_ip {mongo_host} --dbpath {self.mongo_path} --logpath {self.mongo_log}/mongod.log" \
    #             " --fork".format(**self.data, auth=auth)
    command = f"mongoimport --host localhost:27017 --db {dbname} --collection {collname} --file /{fpath}/{fname} --mode {fmode} --type {ftype}"
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, shell=True)
