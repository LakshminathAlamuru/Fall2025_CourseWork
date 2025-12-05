#!/bin/bash

#Detect source file
if [[ -f /proc/cpuinfo ]]; then
	INPUT_FILE="/proc/cpuinfo"
else
	INPUT_FILE="../../cpuinfo.txt"
fi

OUTPUT_FILE="cpuinfo.txt"

total_processors=$(grep -c '^processor' "$INPUT_FILE")

core_ids=$(grep '^core id' "$INPUT_FILE" | awk '{print $4}')

cache_sizes=$(grep '^cache size' "$INPUT_FILE" | awk '{print $4}')

{
	echo "$total_processors"
	echo "$core_ids"
	echo "$cache_sizes"
} > "$OUTPUT_FILE"
