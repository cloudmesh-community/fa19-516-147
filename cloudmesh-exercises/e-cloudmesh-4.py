# E.Cloudmesh.Common.4
# Develop a program that demonstrates the use of cloudmesh.common.Shell

from cloudmesh.common.Shell import Shell

listdir = Shell.ls("-aux")
print(listdir)