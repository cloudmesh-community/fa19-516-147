#!/usr/bin/env python3

# fa19-516-147 E.Cloudmesh.Common.1
# Develop a program that demonstrates the use of banner, Heading and Verbose


from cloudmesh.common.util import banner
from cloudmesh.common.util import HEADING
from cloudmesh.common.debug import VERBOSE
from cloudmesh.common.debug import Variables

variables = Variables()

variables['debug'] = True
variables['trace'] = True
variables['verbose'] = 10

def getbanner():
    banner("This is banner for cloudmesh exercise1")
    HEADING()

def verdebug():
    verbosedebug ={"Value" : "Verbose"}
    VERBOSE(verbosedebug)

getbanner()
verdebug()