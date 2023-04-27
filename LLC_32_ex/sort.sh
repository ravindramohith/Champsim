#!/bin/bash

# Loop through all files with .txt extension
for file in *.txt
do
  # Extract trace name from file name
  trace=${file%%.*}

  # Extract IPC value from file
  ipc=$(grep "IPC value:" $file | awk '{print $4}')

  # Print trace name and IPC value
  echo "$trace: $ipc"
done | sort -t':' -k2 -n 
