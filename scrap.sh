#!/bin/bash

json_file=repos.json
# Clone repositories
# Clone repositories and archieve only .abap files from the repo
# Read the JSON file and loop through each element
for element in $(jq -c '.[]' $json_file); do
    #echo $element
    BASE_REPO="https://github.com/"
    REPO_URL=$BASE_REPO$(echo $element | sed 's/"//g')
    REPO_NAME=$(echo $element | sed 's/"//g')
    REPO_NAME=$(echo "$REPO_NAME" | sed 's/\//_/g')
    REPO_NAME=${REPO_NAME%%/*} 
    CLONE_DIR="./clone"
    ARCHIVE_NAME="$REPO_NAME.zip"

    if [ -e $ARCHIVE_NAME ]; then
        echo "$ARCHIVE_NAME is already created"
    else 
        echo $REPO_NAME
        # Clone the repository
        git clone $REPO_URL  $CLONE_DIR
        echo "repo cloned"
        cd $CLONE_DIR
        # # Create zip archive of files with the .abap extension
        git archive --format=zip --output="../"$ARCHIVE_NAME HEAD -- "*.abap"
        cd ..
        rm -rf $CLONE_DIR
    fi
done

