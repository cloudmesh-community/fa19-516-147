#!/bin/bash
'''the configuration file (/usr/local/etc/mongod.conf)
the log directory path (/usr/local/var/log/mongodb)
the data directory path (/usr/local/var/mongodb)'''
brew update
brew install mongodb-community@4.2
brew services start mongodb-community@4.2
# sudo service mongodb start