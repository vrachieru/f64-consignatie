#!/usr/bin/env python

from time import strftime, gmtime

def now():
  return strftime('%Y-%m-%d %H:%M:%S', gmtime())

def number(value):
  return float(value.replace('lei', '').replace('.', '').replace(',', '.'))
