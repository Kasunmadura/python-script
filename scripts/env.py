#!/usr/bin/python

# hom to run
# $STAGE=staging ./env.py


import os

#stage = os.environ["STAGE"].upper()

stage  = (os.getenv("STAGE") or "deverlopment").upper()

output = "We 're runnning is %s " % stage

if stage.startswith("PROD"):
    output = "DANGER !!!! -" + output

print(output)
