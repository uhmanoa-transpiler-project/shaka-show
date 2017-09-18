import argparse

def parseSource ():
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
	dict = {'PORT': args.port, 'FileName': args.file, 'Source': sourceList }

	#Close the source file
	source.close()

	#return the dictionary value
	return dict

newDict = parseSource()

print("PORT: " + newDict['PORT'] + "\n")
print("FileName: " + newDict['FileName'] + "\n")

for line in newDict['Source']:
	print(line)

