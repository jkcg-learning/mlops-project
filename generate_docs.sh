#!/bin/bash

# Set the PYTHONPATH to include the src directory
export PYTHONPATH=$PYTHONPATH:$(pwd)/src

# Run pdoc to generate the documentation with Google-style docstrings
poetry run pdoc --docformat google --output-dir docs src
