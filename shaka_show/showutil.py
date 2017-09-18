import argparse

def parseArgs ():

	"""
	Function takes in arguments from a command line.
	If the argument is preceded by '-p' or '--port', the value for the source file's port number is changed from '8888' to the argument value.
	One of the input arguments is the source file; if the argument is empty or if the source file does not exist, return error.
	Function returns a dictionary of the port number, the file name, and the source code of the source file.
	"""

	#parse the input
	parser = argparse.ArgumentParser()

	#optionally check for a port number input; if no input, default port number to 8888
	parser.add_argument("-p", "--port", help="assigns the port number", default="8888");

	#Check for source file input; if no input, return error
	parser.add_argument("file", help="reads in the source file name");

	#Assign parsed components to 'args'
	args = parser.parse_args()

	# Open source file and append each line of code to a list
	source = open(args.file, "r")
	sourceList = []
	for line in source:
		sourceList.append(line)

	# Create a dictionary containing the 'port number,' the 'file name,' and the 'source code' of the source file
	newDict = {'port': args.port, 'filename': args.file, 'source': sourceList }

	#Close the source file
	source.close()

	#return the dictionary value
	return newDict
