# cloudmesh excercise 2
#develop a program that demostrate a use of dotdict

from cloudmesh.common.dotdict import dotdict

mydata = { "name":"Harsha" , "course":"MSDS" ,"university" : "Indiana"}

data = dotdict(mydata)

print(data.name)
print(data.course)
print(data.university)