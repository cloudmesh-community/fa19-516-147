# Abstract Database Management On NoSQL Environments

## Objective

Abstract database management on NoSQL environments for the NIST Big Data Reference Architecture and introduce new feature for database opeartions in abstract database management using SQL and NoSQL databases.

## Introduction

We will be providing database abstraction management focused on No SQL technology . 
This will also include addition of new functionality in order to perform databsase operationa more effectively.

* Functionality to pull records from database table into a file
* Introduced functionality (POST) to upload data from file to a database table
* Create and expand functionality for No SQL database like MongoDB or one other
* Enhance GET and PUT request to get or insert data based on specific criteria
* Create docker / container image to deploy and manage

## Implementation Plan 

Abstract Database Management projects provides ability to perform
database operations as a service using Open API connexion service and
reading specification from yaml file designed based on existing NIST
template. Three main components of database service are:

* server.py 
* database_nosql.yaml
* database_nosql.py

### Step 1: NoSQL MongoDB setup

Create Database instance and a database on MongoDB
 
### Step 2: Open API .yaml file

Use NIST database.yaml template file from NIST git directory

[NIST database.yaml](https://github.com/cloudmesh/cloudmesh-nist/blob/master/spec/database.yaml)

#### API Specification database.yaml

NIST API template database.yaml for this database abstraction project is
enhanced keeping no SQL databases as main a focus. 

Key points to keep in mind while working with no SQL databases:


*SQL and NoSQL terminologies*: 

|**SQL Database**| **No SQL Database**|
-----------------|--------------------|
| Database       | Database           |
| Table          | Collection         |
| Row            | Document           |
| Column         | Field              |
| Schema (static)| Schema Dynamic     |



##### YAML File Path and Methods

Path: /database

* get
* put 
* delete

Path: /database/{dbname}/collection/{collname}

This path is a new addition to the current NIST template. This is introduced to perform following table level operations:
 
 * search a named collection in a database schema or list all collections in the database 
 * create a named collection in a database schema
 * delete a named collection in a database schema
 
   ```
    "cloudmesh.database.get_coll" 
    "cloudmesh.database.put_coll" 
    "cloudmesh.database.delete_coll" 
   ```
   
Path: /database/{dbname}/collection/{collname}/data


* get
* put
* delete
* post

Path: /database/{dbname}/collection/{collname}/index/{idx}

* get
* put

## References
