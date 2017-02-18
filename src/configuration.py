#!/usr/bin/env python

from json import load

configurationFile = 'config.json'

class Configuration(object):
  def __init__(self, obj = None):
    self._obj = self.load() if obj is None else obj

  def load(self):
    with open(configurationFile, 'r') as data:
      return load(data)

  def __getattr__(self, key):
    try:
      return Configuration(self._obj[key])
    except (KeyError, AttributeError, IndexError, TypeError):
      return None

  __getitem__ = __getattr__

  def __repr__(self):
    return self._obj