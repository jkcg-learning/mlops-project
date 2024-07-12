#!/bin/bash

# Backup the current changelog
cp CHANGELOG.md CHANGELOG.md.bak

# Generate the new changelog incrementally
cz changelog --unreleased-version $(date +%Y-%m-%d) --incremental

# Append the new changelog to the old one
cat CHANGELOG.md.bak >> CHANGELOG.md

# Remove the backup
rm CHANGELOG.md.bak
