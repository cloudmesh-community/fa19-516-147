############################################################################
# database.py is to create database ,scheme ,table and query in Azure      #
# Section azuresqldb added in the file                                     #
############################################################################

import argparse
import sys
import pyodbc
from flask import jsonify , request
import json
import yaml
from cloudmesh.configuration.Config import Config
from cloudmesh.common.dotdict import dotdict
import collections
#import requests
#import urllib.request


############################################################################
# Read database connection detail from .cloudmesh/cloudmesh.yaml file      #
# Section azuresqldb added in the file                                     #
############################################################################

cloud_service_name = 'aws'
config = Config()
credential= dotdict(config[f"cloudmesh.database.{cloud_service_name}.credentials"])

server = 'absdb.c7n1akxzr3n1.us-east-2.rds.amazonaws.com'
database = credential.database
username = credential.username
password = credential.password
driver= credential.driver

#########################################################################################
# Function for database operations                                                      #
# get database list, connect , disconnect a database                                    #
#########################################################################################

def get():
    con = pyodbc.connect('DRIVER=' + driver + ';SERVER=' + server + ';PORT=1433;DATABASE=' + database + ';UID=' + username + ';PWD=' + password)
    cur = con.cursor()
  #  if dbname.upper() == 'ALL' or (len(dbname) == 0):
    string =  "SELECT name FROM sys.databases"
   # else:
    #    string = "SELECT name FROM sys.databases where name = '""" + dbname + "'"
    db_name1=cur.execute(string)
    rows = cur.fetchall()
    row_array=[]
    for row in rows :
        t=(row.name)
        row_array.append(t)
        j = json.dumps(row_array)
    con.close()
    return json.dumps(row_array)
#############################################
def put(dbname):
    con = pyodbc.connect('DRIVER=' + driver + ';SERVER=' + server + ';PORT=1433;DATABASE=' + database + ';UID=' + username + ';PWD=' + password)
    cur = con.cursor()
    con.autocommit = True
    string = 'CREATE database ' + dbname
    cur.execute(string)
    cur.commit()
    con.close()
###########################################

def delete(dbname):
    con = pyodbc.connect('DRIVER=' + driver + ';SERVER=' + server + ';PORT=1433;DATABASE=' + database + ';UID=' + username + ';PWD=' + password)
    cur = con.cursor()
    con.autocommit = True
    string = 'DROP DATABASE ' + dbname
    cur.execute(string)
    cur.commit()
    con.close()

#########################################################################################
# Function for Schema operations                                                        #
# get list of schema's , put new schema and delete from a database                      #
# Query to gety Schema by Schema owner ,filter by schema_owner ='dbo                    #
# select s.name as schema_name, s.schema_id,u.name as schema_owner from                 #
# sys.schemas s inner join sys.sysusers u on u.uid = s.principal_id order by s.name     #
#########################################################################################


def get_schema(dbname , schname):
    con = pyodbc.connect('DRIVER=' + driver + ';SERVER=' + server + ';PORT=1433;DATABASE=' + database + ';UID=' + username + ';PWD=' + password)
    cur = con.cursor()
    string = "select name from sys.schemas"
    schema_nm = cur.execute(string)
    rows = cur.fetchall()
    row_array = []
    for row in rows:
        t = (row.name)
        row_array.append(t)
        j = json.dumps(row_array)
    con.close()
    # con.commit()
    return json.dumps(row_array)

# ****** Function to create a schema in a database , database name is a input parameter for this function ******


def put_schema(name):
    con = pyodbc.connect('DRIVER=' + driver + ';SERVER=' + server + ';PORT=1433;DATABASE=' + database + ';UID=' + username + ';PWD=' + password)
    cur = con.cursor()
    string = 'CREATE SCHEMA ' + name
    cur.execute(string)
    cur.commit()
    con.close()

# ****** Function to delete schema from database *******


def delete_schema(name):
    con = pyodbc.connect('DRIVER=' + driver + ';SERVER=' + server + ';PORT=1433;DATABASE=' + database + ';UID=' + username + ';PWD=' + password)
    cur = con.cursor()
    string = 'DROP SCHEMA ' + name
    cur.execute(string)
    cur.commit()
    con.close()

#########################################################################################
# Function for table operations                                                         #
# put new table and delete from a database                                              #
#########################################################################################


def get_table(dbname, schname ,tblname):

    con = pyodbc.connect('DRIVER=' + driver + ';SERVER=' + server + ';PORT=1433;DATABASE=' + database + ';UID=' + username + ';PWD=' + password)
    cur = con.cursor()
   # string = "SELECT COLUMN_NAME FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME = '""" + tblname + """'  AND TABLE_SCHEMA = '""" + name + "'"
   # string = "SELECT TABLE_NAME FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_CATALOG = '""" + schname + """'  AND TABLE_SCHEMA = '""" + tblname + "'"
    string = "SELECT TABLE_NAME FROM """ + dbname + """.INFORMATION_SCHEMA.TABLES WHERE TABLE_CATALOG = '""" + dbname + """'  AND TABLE_SCHEMA = '""" + schname + "'"
    table_nm = cur.execute(string)
    rows = cur.fetchall()
    row_array = []
    for row in rows:
      #  t = (row.COLUMN_NAME)
        t = (row.TABLE_NAME)
        row_array.append(t)
        j = json.dumps(row_array)
    con.close()
    # con.commit()
    return json.dumps(row_array)

# ****** Function to create a table in a database , database name is a input parameter for this function ******


def put_table(dbname, schname, tblname):
    con = pyodbc.connect('DRIVER=' + driver + ';SERVER=' + server + ';PORT=1433;DATABASE=' + database + ';UID=' + username + ';PWD=' + password)
    cur = con.cursor()
  #  string = 'CREATE table ' + name.tblname
    string ='create table {0}.{1}.{2}'.format(dbname,schname, tblname)
    cur.execute(string)
    cur.commit()
    con.close()

# ****** Function to delete table from database *******


def delete_table(dbname, schname, tblname):
    con = pyodbc.connect('DRIVER=' + driver + ';SERVER=' + server + ';PORT=1433;DATABASE=' + database + ';UID=' + username + ';PWD=' + password)
    cur = con.cursor()
    string = 'drop table {0}.{1}.{2}'.format(dbname, schname,  tblname)
    cur.execute(string)
    cur.commit()
    con.close()

#########################################################################################
# Function for data operations                                                          #
# get data , upload data and delete data from a database                                #
#########################################################################################

# ******Function to get data from a database table ******


def data_get_old(dbname , schname, tblname):

    con = pyodbc.connect(
        'DRIVER=' + driver + ';SERVER=' + server + ';PORT=1433;DATABASE=' + database + ';UID=' + username + ';PWD=' + password)
    cur = con.cursor()
    string = 'select * from  {0}. {1}. {2}'.format(dbname, schname,  tblname)
    query_out = cur.execute(string)
    rows = cur.fetchall()
    row_array = []
    for row in rows:
        t = (row.name)
        row_array.append(t)
        j = json.dumps(row_array)
    con.close()
    return json.dumps(row_array)


def data_get(dbname ,schname , tblname):
    #outfile = open(tblname.json, 'w')
    objects_list = []
    con = pyodbc.connect('DRIVER=' + driver + ';SERVER=' + server + ';PORT=1433;DATABASE=' + database + ';UID=' + username + ';PWD=' + password)
    cur = con.cursor()
    string = 'select * from  {0}. {1}. {2}'.format(dbname, schname,  tblname)
    cur.execute(string)
    columns = [i[0] for i in cur.description]
    allrows = cur.fetchall()

    #outfile.write('<?xml version="1.0" ?>\n')
    #outfile.write('<tabledata>\n')
       # outfile.write('  <row>\n')
        #columnNumber = 0
        #for column in columns:
        #    data = rows[columnNumber]
          #  if data == None:
         #       data = ''
          #  outfile.write('<%s>%s</%s>' % (column, data, column))
          #  columnNumber += 1
     #   outfile.write('  </row>\n')
    #outfile.write('</tabledata>\n')
   # outfile.close()
   # return (outfile)
    #return json.dumps(outfile)
    for row in allrows:
        d = collections.OrderedDict()
        columnNumber = 0
        for column in columns:
            d[column] = row[columnNumber]
            columnNumber += 1
        objects_list.append(d)
    con.close()
    return json.dumps(objects_list)


# ******Function to load data into a database table ******


def data_put(dbname , schname , tblname):
    #DATA = b'some data'
    #req = urllib.request.Request(url='http://localhost:8080', data=DATA, method='PUT')
    #with urllib.request.urlopen(req) as f:
    #    pass
    #print(f.status)
    #print(f.reason)

    con = pyodbc.connect('DRIVER=' + driver + ';SERVER=' + server + ';PORT=1433;DATABASE=' + database + ';UID=' + username + ';PWD=' + password)
    cur = con.cursor()
    data_dict = request.json
    string = 'insert into  {0}.{1}.{2}'.format(dbname, schname, tblname)
    key = list(data_dict.keys())
    key1 = str(key)
    key2 = key1.replace('[', '(')
    key3 = key2.replace(']', ')')
    key4 = key3.replace("'", "")
    print(key4)
    val = list(data_dict.values())
    val1 = str(val)
    val2 = val1.replace('[', '(')
    val3 = val2.replace(']', ')')
    query = string + key4 + "values" + val3

    cur.execute(query)
    cur.commit()
    con.close()


# ******Function to delete data into a database table ******


def data_delete(dbname , schname, tblname):
     query_param = request.args
     col1 = query_param.get('col1')
     val1 = query_param.get('val1')
     con = pyodbc.connect('DRIVER=' + driver + ';SERVER=' + server + ';PORT=1433;DATABASE=' + database + ';UID=' + username + ';PWD=' + password)
     cur = con.cursor()
     string = 'delete from {0}.{1}.{2}'.format(dbname, schname, tblname)

     cur.execute(string)
     cur.commit()
     con.close()

def data_get_file(outfileName , query):
    outfile = open(outfileName, 'w')
    con = pyodbc.connect('DRIVER=' + driver + ';SERVER=' + server + ';PORT=1433;DATABASE=' + database + ';UID=' + username + ';PWD=' + password)
    cur = con.cursor()
    string = query
    cur.execute(string)
    rows = cur.fetchall()
    outfile.write('<?xml version="1.0" ?>\n')
    outfile.write('<tabledata>\n')
    for row in rows:
        outfile.write('  <row>\n')
        outfile.write('    <name>%s</name>\n' % row[0])
        outfile.write('    <id>%s</id>\n' % row[1])
        outfile.write('    <status>%s</status>\n' % row[2])
        outfile.write('  </row>\n')
    outfile.write('</tabledata>\n')
    outfile.close()
    return (outfile)
"""
#crom cloudmesh.configuration.Config import C\onfog

#config = COnfig()


#azure credentials = config['cloudmesh.database.azure.credentials']
#
# you have to define what credentials look like, see the existing examples for compute and storage.

#improvement to the nist spec
#
#in the nist spec we have

#cloudmesh.database.get.schema"

#but we need
# cloudmesh.database.get_schema
#

def get_schema():
    print("get the schema")

def connect():
    # start the connection to the db from config
    pass

def disconnect():
    pass

def put_data():
    pass
def put_schema():
    pass
def delete():
    pass
def data():
    pass

def query(string):
    pass

# other stuff
"""