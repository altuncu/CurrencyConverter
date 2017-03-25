#!/usr/bin/python

import json
import urllib2

def convert(curr1, curr2, val):
    if curr1 == curr2:
        return str(val)
    else:
        url = urllib2.urlopen("http://api.fixer.io/latest?base=" + curr1)
        data = json.load(url)
        return str(data['rates'][curr2] * val)
