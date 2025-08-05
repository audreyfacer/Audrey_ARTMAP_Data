#!/bin/bash
# -----------------------------------------------------------------------------
#
# File: init.sh
#
# Author: Sasha Petrenko <petrenkos@mst.edu>
# Date: 7/14/2023
#
# Description:
#
#   This is a bash script outlining the setup process necessary to get up and
#   running with this project in a linux environment. It loads the python
#   module, creates the virtual environment, and sources (loads) the virtual
#   environment that we just created.
#
# -----------------------------------------------------------------------------

# This is the way to define variables in bash scripts
ENV_NAME=audrey
ENV_DIR=$HOME/.venv
ENV_PATH=$END_DIR/$ENV_NAME

# We will make the directory .venv at the user home (~).
# Putting your python virtual environments in .venv is good practice.
mkdir -p $ENV_DIR

# Load the python module on the cluster
module load python

# Run the venv script, creating the environment
python3 -m venv $ENV_PATH

# Activate the environment
source $ENV_PATH/bin/activate

# Install dependencies
pip install -r requirements.txt
