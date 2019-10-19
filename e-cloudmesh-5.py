# E.Cloudmesh.Common.5
# Develop a program that demostrate a use of cloudmesh.common.StopWatch

from cloudmesh.common.StopWatch import StopWatch
from time import sleep

StopWatch.start("My stop watch")
sleep(2)
StopWatch.stop("My stop watch")
print(StopWatch.get("My stop watch"))