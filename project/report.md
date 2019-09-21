##  Database abstraction in muilti cloud environments

fa19-516-147, Harsha Upadhyay

## Objective

We will be providing database abstractions to host arbitrary databases in arbitrary cloud environments.In order to verify that the database provisioning multi cloud environment works , we will be providing a detailed test to manipulate data in database. This will include standard database functionality.The implementation is being conducted as part of API REST services and we will be using following clouds: 
1. Amazon
1. Azure 
1. and Local DB
We will be providing pytest to deploy and execute the verification of the correctness of this services.

## Design Components 

* Source Data / File residing in cloud or On-prim
* Data abstract
* Target table design (in multiple cloud) 
* REST API design (to surface data from cloud table and make availble for consumtion )

## Technology Used

* Source : CSV File
* Target Infrastucture : AWS Cloud  & Azure (as project requirements there should two cloud included, will use one which are available free or low cost)
* Target DB : willing to use Aurora or redshift but have to deside based on availability
* API : REST
* Code : Python
* Virtual Config : Cloudmesh

## Architecture & Design Detail 

Architecture Diagram 

### Pipeline Design
   
TBD
 
### Cloud Target Table 

TBD

### REST API
TBD

## Conclusion
