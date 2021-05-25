#!/usr/bin/python3
from sys import argv
from os import popen
from os import system

home = (popen("echo $HOME")).read().rstrip()
now = (popen('date "+%F %R:%S"')).read().rstrip()

FILE_LOC = home+"/Documents/bb.txt"

#TODO: Add "-i" interactive mode for doing more stuff
if(len(argv)<2):
	print("Usage:\n\tbb.py <words to search>\n\tbb.py -w <words to write>\n\tbb.py -a # Prints contents of the entire file")
	exit()
elif(argv[1]=="-w"):
	to_write = now+" "+home+"> "+" ".join(argv[2:]) + "\n"
	print("Writing in "+FILE_LOC  +"\n--------------------")
	with open(FILE_LOC, "a") as my_file:
		my_file.write(to_write)
		print(to_write)
	print("--------------------\n")
elif(argv[1]=="-e"):
        print("--------------------\nEditing "+FILE_LOC+"\n")
        system("nano "+FILE_LOC)
        print("Finished editing "+FILE_LOC+"\n--------------------\n")

elif(argv[1]=="-a"):
	print("contents of "+FILE_LOC+"\n--------------------")
	for line in open(FILE_LOC):
		print(line)
	print("--------------------\n")

else:
	to_search = ' '.join(argv[1:])
	print("Searching in "+FILE_LOC+" for "+to_search+"\n--------------------")
	for line in open(FILE_LOC):
		if to_search in ">".join(((line.split(">"))[1:])):
			print(line)
	print("--------------------\n")
