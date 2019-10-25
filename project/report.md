# Abstract Database Management On Multicloud Environments (with focus on Azure and AWS3)

Harsha Upadhyay, [fa19-516-147](https://github.com/cloudmesh-community/fa19-516-147/edit/master/project/report.md)

## Objective

Abstract database management on Multicloud environments for the NIST Big Data Reference Architecture AWS, Azure.

## Introduction

We will be providing database abstractions to host arbitrary databases in arbitrary 
cloud environments. In order to verify that the database provisioning multi cloud 
environment works, we will be providing a detailed test to manipulate data in database. 
This will include standard database functionality. The implementation is being conducted as 
part of API REST services and we will be using following clouds: 

1. Amazon
1. Azure 
1. and Local DB

We are providing pytests to deploy and execute the verification of the correctness of this services.

## Comparison of Cloud Database Services 


|Azure                          | AWS                      |    Google                 |Oracle                             | IBM                                  |MongoDB      |
|-------------------------------| -------------------------|---------------------------|-----------------------------------|--------------------------------------|-------------|
| Cosmos DB                     | Auora                    | Cloud SQL                 | Autonomous Data Warehouse         | IBM Cloudant                         |MongoDB Atlas|
| SQL Database                  | RDS                      | Cloud Spanner             | Autonomous Transaction Processing | IBM Cloud Databases for MongoDB      |             | 
| Database for MySQL            | Redshift                 | Cloud Bigtable            | Database Cloud Service–Bare Metal | IBM Cloud Databases for Elasticsearch|             |
| Database for PostgreSQL       | DynamoDB                 | Cloud Firestone           | Database on virtual machines (VMs)| IBM Cloud Databases for etcd         |             |
| Database for MariaDB          | ElastiCache for Memcached| Firebase realtime Database| Exadata Database Machine          | IBM Cloud Databases for PostgreSQL   |             |                       
| SQL Server on Virtual Machines|ElastiCache for Redis     | Cloud Memory Store        | Database Exadata Cloud at Customer| IBM Cloud Messages for RabbitMQ      |             |
| Database Migration Service    | DocumentDB               |                           | NoSQL Database                    | IBM Compose for JanusGraph           |             |
| Cache for Redis               | Neptune                  |                           |                                   | IBM Db2 on Cloud                     |             |
| Table Storage                 | Timestream               |                           |                                   | IBM Db2 Warehouse on Cloud           |             |
| Data Explorer                 | QLDB                     |                           |                                   | IBM Compose for ScyllaDB             |             |
| Database for MariaDB          |                          |                           |                                   | Hyper Protect DBaaS for MongoDB      |             |
|                               |                          |                           |                                   | Hyper Protect DBaaS for PostgreSQL   |             |    


## Overview of Cloudmesh

Why ..Motivation..

## Requirements

* file based:

* recursive tree
* Transfer queue 
* Command shell
* Rest API
* Python API


## Architecture 

Architecture Diagram & Details 

## Technology detail

 * AWS Redshift/ RDS  & Azure SQL Database
 * REST / Open API
 * Python Scripting
 * Cloudmesh

## Implementation Plan 

 ### Step 1: Database Object Creation
   Create Database objects like tables ,views  on a cloud DB (Azure SQL Database )
   Python script to create objects 
 
 ### Step 2: Open API .yaml file
   Create a yaml file 
     * to get database , schema and DDL listing from one cloud environment (e.g Azure or AWS)
     * to create/copy database schema and DDL in other cloude environment 
        
        database.yaml
 ### Step3: Setup Config file
   Create a config file with environment detail for all environment used in the project
   
        cloudmesh.yaml 
  
 ### Step4 : Integration with cloudmesh 
   Set up command line 
  
## Benchmarks

## Conclusion

## Progress
  * Azure account created
  * A database created on Azure SQL Database
  * Docker setup on local
  * Python script to test connection to databse and deploy table
  * AWS account creation

## Workbreakdown


|Due Date | Project Task                      | Breakdown                                   |
|---------|-----------------------------------| --------------------------------------------|
|         | report.md file                    | report.md file creation in hid directory    |
|         |                                   | Technology selection                        |
|         |                                   | Finalize Design components                  |
|         |                                   | Infrastructure set up                       |
|10/18    | Project Review                    |                                             |
|12/02    | Project Due                       |                                             |
|12/09    | Project Final(No Grade Penalty)   |                                             |
|12/18    | Project Due with Penalty          |                                             |

## Refernces

1. <https://cloud.google.com/python/docs/reference/>
1. <https://github.com/googleapis/google-cloud-python#google-cloud-python-client>
1. <https://github.com/cloudmesh/cloudmesh-storage/blob/master/cloudmesh/storage/spec/openapi_storage.yaml>
1. <https://github.com/cloudmesh/cloudmesh-nist/blob/master/spec/database.yaml>
1. Azure SQL Database <https://azure.microsoft.com/en-us/services/sql-database/>
1. Azure Cloud Database Services <https://azure.microsoft.com/en-us/product-categories/databases/>
1. AWS Cloud Database Services <https://aws.amazon.com/products/databases/>
1. Google Cloud Database Servcies <https://cloud.google.com/products/databases/?hl=pl>
1. Oracle Cloud Database Services <https://www.oracle.com/database/cloud-services.html>
1. IBM Cloud Database Services <https://www.ibm.com/cloud/databases>
1. MongoDB Cloud Databse Servcies <https://www.mongodb.com/cloud> 