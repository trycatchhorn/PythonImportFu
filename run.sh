#!/usr/bin/env bash

python3 main.py

find . -name "*.py~" -type f -delete
find . -name "*.pyc" -type f -delete
find . -name "__pycache__" -type d -delete

