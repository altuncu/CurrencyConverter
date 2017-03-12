#!/usr/bin/python

import json
import urllib2

def convert(curr1, curr2, val):
    url = urllib2.urlopen("http://api.fixer.io/latest?symbols=" + curr1 + "," + curr2)
    data = json.load(url)
    return data['rates'][curr2]
