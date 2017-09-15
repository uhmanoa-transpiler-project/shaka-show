import argparse
parser = argparse.ArgumentParser()
parser.add_argument("--port", help="assigns the port number");
parser.add_argument("file", help="reads in the source file name");
args = parser.parse_args()

if args.port:

	print("PORT: " + args.port)


print("Source File: " + args.file)

source = open(args.file, "r")
for line in source:
	print(line)



source.close()

