# Abstract Database Management On Multicloud Environments (with focus on Azure and AWS3)

Harsha Upadhyay, [fa19-516-147](https://github.com/cloudmesh-community/fa19-516-147/edit/master/project/report.md)

:o: put in url to python api for google in Refernces section

:o: start looking at cloudmesh-storage  

:o: use proper punctioation space rules there is a space after a , . and so on but not before

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

## Related Work


## Technology detail

 * AWS Redshift  & Azure SQL Database
 * REST / Open API
 * Python Scripting
 * Cloudmesh

## Architecture 

Architecture Diagram & Details 

## Implementation Plan 

 ### Step 1: Database Object Creation
   Create Database objects like tables ,views  on a cloud DB (Azure SQL Database )
   Python script to create objects 
 
 ### Step 2: Open API .yaml file
   Create a yaml file 
     * to get database , schema and DDL listing from one cloud environment (e.g Azure or AWS)
     * to create/copy database schema and DDL in other cloude environment 
 
 ### Step3: Setup Config file
   Create a config file with environment detail for all environment used in the project
  
 ### Step4 : Integration with cloudmesh 
   
  
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
