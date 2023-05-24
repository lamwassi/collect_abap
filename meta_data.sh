#! bin/bash
user_file="test.json"
base_api="https://api.github.com/" 
endpoint="repos/"
# # Read the JSON file and loop through each element
for element in $(jq -c '.[]' $user_file); do
    echo "$element"
    REPO_URL=$base_api$endpoint$(echo $element | sed 's/"//g')
    echo $REPO_URL
    curl -L  -H "Accept: application/vnd.github+json" -H "Authorization: Bearer <token>"  -H "X-GitHub-Api-Version: 2022-11-28" $REPO_URL          #| jq -r '.html_url' | jq '.[] | {html_url,languages_url,ssh_url,clone_url}' >> repo_urls.json
   done
