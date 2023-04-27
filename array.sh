#!/bin/bash

# Check that a file was provided as an argument
if [ $# -lt 1 ]; then
  echo "Usage: $0 <input file>"
  exit 1
fi

# Extract the IPC values from the input file
mapfile -t arr < <(grep "$1" "$2.txt" | awk '{print $7}')
policy=$(echo $1 | cut -d '-' -f 10)

echo -n "$policy=["
for element in "${arr[@]}"
do
    echo -n "$element"
done

echo "]"

mapfile -t arr < <(grep "$3" "$2.txt" | awk '{print $7}')
policy=$(echo $3 | cut -d '-' -f 10)

echo -n "$policy=["
for element in "${arr[@]}"
do
    echo -n "$element"
done

echo "]"

mapfile -t arr < <(grep "$4" "$2.txt" | awk '{print $7}')
policy=$(echo $4 | cut -d '-' -f 10)

echo -n "$policy=["
for element in "${arr[@]}"
do
    echo -n "$element"
done

echo "]"

mapfile -t arr < <(grep "$5" "$2.txt" | awk '{print $7}')
policy=$(echo $5 | cut -d '-' -f 10)

echo -n "$policy=["
for element in "${arr[@]}"
do
    echo -n "$element"
done

echo "]"

# lfu=$(grep "IPC (LLC) [4,16,32]" $1 | awk '{getline; print $NF}')
# fifo=$(grep "IPC (LLC) [4,16,32]" $1 | awk '{getline; getline; print $NF}')
# random=$(grep "IPC (LLC) [4,16,32]" $1 | awk '{getline; getline; getline; print $NF}')

# Print the IPC values for each replacement policy

# echo "LFU:   $lfu"
# echo "FIFO:  $fifo"
# echo "Random: $random"
