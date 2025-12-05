#!/bin/bash

# Create a temp dir
mkdir -p tmp_cfiles
# Copy only filenames (strip path) 
find . -type f -name "*.c" -exec cp {} tmp_cfiles/ \;
# Create tar from temp dir 
tar -cvf allcfiles.tar -C tmp_cfiles . 
# Cleanup 
rm -rf tmp_cfiles
