##  Database abstraction in muilti cloud environments

fa19-516-147, Harsha Upadhyay

## Objective

We will be providing database abstractions to host arbitry databases in arbitary cloud environments.I norder to varify trhat the databse provision;ing multi cloud env works we will be providing a detailed test to manupulate data indatbase , this will incljude standerd datbase functionality.The implemention is being is cunduded as part of API rest services and we will be using following clud . amazon, azure and local db . we will bb eproviding pytest to deploy and execute thye verification iof the correctness of this services


Objective of this project is to perform data management activities on Cloud DB by abstracting ,loading and accessing databases into Cloud DB.

/%Objective of this project is to design and implement data pipeline to load CSV data into Cloud environment and make it available for consumption through REST API.%/

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
