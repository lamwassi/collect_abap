#!/bin/bash
# Define the path to the JSON file
json_file="/app/repos.json"

# Read the JSON file and loop through each element
for element in $(jq -c '.[]' $json_file); do
    # Print the element to the console
    #echo $element
    BASE_REPO="https://github.com/"
    REPO_URL=$BASE_REPO$(echo $element | sed 's/"//g')
    REPO_NAME=$(echo $element | sed 's/"//g')
    REPO_NAME=${REPO_NAME%%/*} 
    CLONE_DIR="/app/cl"
    ARCHIVE_NAME="/app/$REPO_NAME.zip"
    # Add additional commands to process the element as needed
    # Clone the repository
    git clone $REPO_URL $CLONE_DIR
    # Create zip archive of files with the .txt extension
    cd $CLONE_DIR
    git archive --format=zip --output=$ARCHIVE_NAME HEAD -- "*.abap"
    cd ..
    rm -rf $CLONE_DIR

done
