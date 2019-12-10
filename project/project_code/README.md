# Abstract Database Management on Multicloud Environment 

## Steps 

* Install Python3.x.x environment  
  Download from Python.org <https://www.python.org/downloads/>

* Activate your Python environment.

* Install requirements.txt 
```
pip install -r requirements.txt
```
* Install cloudmesh 
  Follow installation steps from Cloudmesh Manual <https://cloudmesh.github.io/cloudmesh-manual/>

* Create cloud account and database instance on cloud environment 
AWS RDS  SQL Server Express Edition 
* Start the server 
```
python3 server.py
```

* In the second terminal you run the curl call 

```bash
curl http://localhost:8080/cloudmesh/database
```
