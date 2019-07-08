#!/bin/sh

my_dir=$(dirname "$(readlink "$0")")
cd "$my_dir"
USER="$(python -c 'import config;print(config.username)')" 
DIRECTORY="$(python -c 'import config;print(config.project_directory)')/$1"
python3 create.py $1
if [ -d $DIRECTORY ]; then
    cd "$DIRECTORY"
    git init
    git remote add origin git@github.com:"$USER"/$1.git
    touch README.md
    git add -A
    git commit -m "Initial commit"
    git push -u origin master
    code .
fi