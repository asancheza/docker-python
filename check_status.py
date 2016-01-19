#!/usr/bin/python

"""
Script check urls connections from file
"""

import urllib

def checkConnection():
	with open("urls.txt", "r") as urls:
		for url in urls:
			connection = urllib.urlopen(url)
			print "[" + str(connection.getcode()) + "]" + url

checkConnection()