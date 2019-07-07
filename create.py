import os
import sys
import requests
import json
import config

# User credentials
user = config.username
token = config.token

# Project directory path
project_dir = config.project_directory;

def create():
    headers = {'Authorization': 'token ' + token}
    get_response = requests.get('https://api.github.com/user', auth=(user, token));

    if get_response.ok:
        repo = sys.argv[1];        
        payload = {'name': repo, 'auto_init': 'false'}

        post_reponse = requests.post('https://api.github.com/user/repos', 
        auth=(user,token), data=json.dumps(payload))
        
        if post_reponse.status_code == 201:
            print("Successfully created repository {}/{}.".format(user, repo))
            repo_directory = "{}/{}".format(project_dir, repo)
            if not os.path.exists(repo_directory):
                print("Making directory...")
                os.makedirs(repo_directory)
        else:
            print("Error {}: Failed to create repository.".format(post_reponse.status_code))
    else:
        print("Error {}: Incorrect user credentials.".format(get_response.status_code))

if __name__ == "__main__":
    create()