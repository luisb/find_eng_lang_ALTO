#!/usr/bin/python
import sys

if len(sys.argv) == 1:
	print "FATAL: " + __file__ + " expects to be passed one or more files."
	print "usage: " + __file__ + " file [file]..."
	sys.exit()

import lxml.etree as ET
from StringIO import StringIO

for File in sys.argv:
	if File == __file__:
		continue
	
	# if language == 'eng' proceed to next file
	# use try/except to continue outer loop
	try:
		tree = ET.parse(File)
		
		with open(File,'r') as f:
			# read data form file into "data"
			data = f.read()

			# parse the file in memory
			root = ET.parse(StringIO(data))
	
			# get the TextBlock element and store the language and ID attributes in respective vars, if they exist
			for textblock in root.getiterator('{http://www.loc.gov/standards/alto/ns-v2#}TextBlock'):
				if 'language' in  textblock.attrib:
					lang  = textblock.attrib['language']
					
					# if 'eng' found, print a message to t	hat effect
					if lang == 'eng':
						print File + ': "eng" detected.'
						# "eng" found; proceed to next file
						raise NextFile
	except NextFile:
		continue
