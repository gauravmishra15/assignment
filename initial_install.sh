#! /usr/bin/env bash



##initiate pipenv
pipenv --three

# Must be done in this order
pipenv install -e p3
pipenv install -e p2
pipenv install -e p1