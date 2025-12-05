#!/bin/bash

# create directory Assignment-1
mkdir -p Assignment-1

# Run a loop to create 10 directories inside the Assignment folder as required
for i in {1..10};
do
	# create directory with Query-i name
	mkdir -p "Assignment-1/Query-$i"
	# create the response-i.sh file inside the directory
	touch "Assignment-1/Query-$i/response-$i.sh"
done

