#!/usr/bin/python

"""
Script check urls connections from file
"""

import sys
import urllib
import unittest
import getopt
import threading
import time
#from mock import patch
from multiprocessing import Process

""" 
Status class to check connection
"""
class Status:
	"""
	Connect to url
	"""
	def connect(self, url):
		connection = urllib.urlopen(url)
		sys.stdout.write("[" + str(connection.getcode()) + "] " + url)

	""" 
	Check connection
	"""
	def checkConnection(self):
		with open("urls.txt", "r") as urls:
			for url in urls:
				self.connect(url)

	"""
	Check connection with threads
	"""
	def checkConnectionThreads(self):
		with open("urls.txt", "r") as urls:
			for url in urls:
				t = threading.Thread(target=self.connect, args=(url,))
				t.start()

	"""
	Check connection multiproccessing
	"""
	def checkConnectionMultiprocessing(self):
		with open("urls.txt", "r") as urls:
			for url in urls:
				p = Process(target=self.connect, args=(url,))
				p.start()
				p.join()

"""
Main to call all the options
"""
def main():
	if len(sys.argv) > 2:
		if (sys.argv[2] == "multithreads"):
			status = Status()
			status.checkConnectionThreads()

		if (sys.argv[2] == "multiprocessing"):
			status = Status()
			status.checkConnectionMultiprocessing()
	else:
		status = Status()
		status.checkConnection()

if __name__ == "__main__":
	main()