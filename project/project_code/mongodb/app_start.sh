#!/bin/bash

DATE=`date '+%Y-%m-%d %H%M%S'`
DATE=$(echo "$DATE" | tr ' ' _)
#log_file_name= ~/server_$DATE.log
source ~/ENV3/bin/activate
python server.py
#open http://127.0.0.1:8080/cloudmesh/v3/ui/
#> $log_file_name
#deactivate
