for file in *.txt; do

    # find the line that contains "Cumulative IPC"
    lin=$(grep "LLC ways:" $file)
    lin=$(echo $lin | awk '{print $3}')
    line=$(grep "CPU 0 cumulative IPC" $file)
    line2=$(grep "LLC TOTAL" $file)
    
    # extract the value of cumulative IPC
    value=$(echo $line | awk '{print $5}')
    value2=$(echo $line2 | awk '{print $4}')
    value3=$(echo $line2 | awk '{print $8}')
    Vn="0.01"
    Vn=$(echo "scale=2; $Vn" | bc)
    value3=$(echo "scale=5; $value3" | bc)
    value2=$(echo "scale=5; $value2" | bc)
    value2=$(echo "scale=5; $value3 / $value2" | bc)
    value2=$(echo "scale=3; $value2 / $Vn" | bc)
    # $value3 = $value3/$value2
    # print the value of cumulative IPC for this file
    echo "$file: LLCWAYS = $lin, IPC value: $value, Missrate: $value2"

done
