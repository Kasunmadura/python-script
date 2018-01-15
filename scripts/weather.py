#!/usr/bin/env python

## we can use virtualenv for test this
##    pip install --user Virualenv
##    which virtualenv
##    ls /.local/bin/virtualenv
#source venvs/experiment/bin/activate

## you have to Login to openweathermap.org and create API key  and use it as below
#OWM_API_KEY=d052cea9f8275e63565c9c5dsdsdbafe79 ./weather.py 23456

import sys
import os
import requests
from argparse import ArgumentParser
#print(requests.__file__)

parser = ArgumentParser(description= 'Get the current weather information')
parser.add_argument('zip', help= 'zip/postal code to get the weather for ')
parser.add_argument('--country',default='us', help= 'country zip/postal belongs to ,default is "US"')


args = parser.parse_args()

url  = "http://api.openweathermap.org/data/2.5/weather?zip=%s,%s&appapi=%s" % (
        args.zip,
        args.country,
        os.getenv("OWM_API_KEY")
        )

res = requests.get (url)

if res.status_code !=200:
    print ("Error talking to weather provider : %s" % res.status_code)
    sys.exit(1)

print(res.json())
