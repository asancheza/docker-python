#!/usr/bin/python

"""
Script check urls connections from file
"""

import sys
import urllib
import unittest
import getopt
import threading
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
		print "[" + str(connection.getcode()) + "] " + url

	""" 
	Check connection
	"""
	def checkConnection(self):
		with open("urls.txt", "r") as urls:
			for url in urls:
				connect(self, url)

	"""
	Check connection with threads
	"""
	def checkConnectionThreads(self):
		threads = []

		with open("urls.txt", "r") as urls:
			for url in urls:
				t = threading.Thread(target=connect, args=('url'))
				threads.append(t)
				t.start()

	"""
	Check connection multiproccessing
	"""
	def checkConnectionMultiprocessing(self):
		threads = []
		
		with open("urls.txt", "r") as urls:
			for url in urls:
				p = Process(target=connect, args=('url'))
    		p.start()
    		p.join()

"""
Main to call all the options
"""
def main():
	print sys.argv[0]
	status = Status()
	status.checkConnection()
	status.checkConnectionThreads()
	status.checkConnectionMultiprocessing()

if __name__ == "__main__":
	main()