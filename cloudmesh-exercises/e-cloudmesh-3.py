# E.Cloudmesh.Common.3
# Develop a program that demostrate the use of FlatDict

from cloudmesh.common.FlatDict import FlatDict

mydata = {
    "name" : {"first" : "harsha" , "last" : "upadhyay" } ,
    "edu" : {"subject" : "Cloud Computing" , "program" : "MSDS",  "university" : "Indiana University"}
}

mydata = FlatDict(mydata)
print(mydata)