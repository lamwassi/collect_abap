#!/bin/bash
  
temp_dir="./temp"

# Retrieve all ".zip" files in the directory and store them in an array
txt_files=("."/*.zip)

count=0
# Print each file name
for file in "${txt_files[@]}"; do
    mkdir $temp_dir
    unzip "$file" -d $temp_dir
    cd $temp_dir
    num=0
    num=$(find  .  -type f -name "*.abap" | grep -c "")
    ((count+=num))
    cd ..
    echo "counted"
    rm -rf $temp_dir
done
echo $count

