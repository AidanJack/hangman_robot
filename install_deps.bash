#!/bin/bash

# Script to install Python dependencies and ffmpeg

# Update and install ffmpeg
echo "Updating package lists and installing ffmpeg..."
sudo apt-get update -y && sudo apt-get install -y ffmpeg

# Check if pip_requirements.txt exists
if [ -f "pip_requirements.txt" ]; then
    echo "Installing Python dependencies from pip_requirements.txt..."
    pip install -r pip_requirements.txt
else
    echo "Error: pip_requirements.txt not found in the current directory."
    exit 1
fi

echo "Installation complete!"