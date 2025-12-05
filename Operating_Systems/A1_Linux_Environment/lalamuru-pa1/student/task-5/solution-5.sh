#!/bin/bash

#step1: Download the sample data tar file
URL="$1"
downloaded_filename="sample_data.tar"
parent_file="../../$downloaded_filename"

# Check if the tar file exists in the parent folder
if [ -f "$parent_file" ]; then
	: # do nothing
else
    wget -O "$downloaded_filename" "$URL"
    # Move it to the parent folder
    mv "$downloaded_filename" ../..
fi

#step2: Extract the tar file in the current directory
tar -xvf "$parent_file"

mkdir -p smart
mkdir -p OS

out_file="result.txt"
> "$out_file"

#step3: count "smart" string apperances in the file
for f in sample_data/*;
do
	#count apperances
	smart_count=$(grep -o -i "smart" "$f" | wc -l)

	printf "%s smart %d\n" "$f" "$smart_count" >>"$out_file"

	if [ "$smart_count" -gt 0 ]; then
		cp "$f" smart/
	fi
done


#step 4: count "operating system" apperances in the file
for f in sample_data/*;
do
	os_count=$(grep -o -i "operating system" "$f" | wc -l)
	printf "%s operating system %d\n" "$f" "$os_count" >> "$out_file"

	if [ "$os_count" -gt 0 ]; then
		cp "$f" OS/
	fi
done
