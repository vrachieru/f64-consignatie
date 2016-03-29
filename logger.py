#!/usr/bin/env python

from utils import now

logFile = "log"

class Logger():
	def write(self, data):
		with open(logFile, "a+") as f:
			f.write("%s: %s\n" % (now(), data))