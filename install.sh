#!/bin/sh
# install - install a program, script, or datafile

pipenv install --ignore-pipfile
DIR="$( cd "$( dirname "$0" )" && pwd )"
ln -sf "$DIR"/create-project.sh /usr/local/bin/create-project

echo "Installed project creation automation tool successfully!"
echo "To start using, add your github credentials and project directory in the config.py configuration file"
echo "Then, run create-project <project-name> to create a new project!"