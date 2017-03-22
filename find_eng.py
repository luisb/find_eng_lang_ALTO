#!/usr/bin/python
import sys

if len(sys.argv) == 1:
	print "FATAL: " + __file__ + " expects to be passed one or more files."
	print "usage: " + __file__ + " file [file]..."
	sys.exit()

import lxml.etree as ET
from StringIO import StringIO

eng_file_count = 0

for File in sys.argv:
	if File == __file__:
		continue
	
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
			if 'ID' in textblock.attrib: 
				id = textblock.attrib['ID']
			
			# if 'eng' found, print a message to that effect
			if lang == 'eng':
				eng_file_count = eng_file_count + 1
				print File + ': "eng" detected in Textblock ID=' + id + '.'


