#! /usr/bin/env bash

## install python 3.6
$ pipenv install --python 3.6


##initiate pipenv
pipenv --three
export PIP_PROCESS_DEPENDENCY_LINKS=1

# Must be done in this order
pipenv install -e p3 
pipenv install -e p2
pipenv install -e p1
