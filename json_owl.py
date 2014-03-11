import json
import sys
import pprint
import re


def pprintJson(data):
	print "The json file looks like this: \n"
	pprint.pprint(data)
	print

def owlGenerate(data):
	print

if __name__ == '__main__':
	filename = sys.argv[1]
	
	json_data = open(filename)
	data = json.load(json_data)

	# prints a pretty version of the json file before beginning
	pprintJson(data)

	owlGenerate(data)

	# prints the number of "primary keys in the json file"
	print len(data.keys())
	
	# prints key:value pairs for the entirety of the json at the n+1 level
	j= 0
	for i in data.keys():
		j += 1
		print "KEY " + str(j) + ": " + str(i)
		print "VALUE " + str(j) + ": " + str(data[i]) + "\n"

