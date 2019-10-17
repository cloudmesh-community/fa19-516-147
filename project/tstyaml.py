import os
import sys
import yaml

try:
    yamlFilename = os.sys.argv[1]
    yamlFile = open( yamlfilename ,"r")
except:
    print("file does not exist")
    sys.exit()
try:
    yaml.load(yamlFile.read())
except:
    print("valid file")
