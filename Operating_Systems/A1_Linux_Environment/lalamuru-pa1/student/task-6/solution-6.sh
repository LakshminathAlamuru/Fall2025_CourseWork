#!/bin/bash

# extract the tar.gz file

tar -xzf input.tar.gz

#create TXT dir and move all *.txt files to TXT folder
mkdir -p TXT
find input/ -type f -name "*.txt" -exec mv {} TXT/ \;

#create JPG dir and move all *.jpg files to JPG folder
mkdir -p JPG
find input/ -type f -name "*.jpg" -exec mv {} JPG/ \;

#create ZIP dir and move all files without *.txt and *.jpg files to ZIP folder
mkdir -p ZIP
find input/ -type f ! -name "*.txt" ! -name "*.jpg" -exec mv {} ZIP/ \;

#zipping files 
tar -czf "rest zipped.tar.gz" ZIP/
