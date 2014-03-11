import json
import sys
import pprint


def pprintJson(data):
	print "The json file looks like this: \n"
	pprint.pprint(data)
	print

def owlGenerate(data):
	

if __name__ == '__main__':
	filename = sys.argv[1]
	
	json_data = open(filename)
	data = json.load(json_data)

	pprintJson(data)

	owlGenerate(data)
	print len(data.keys())
