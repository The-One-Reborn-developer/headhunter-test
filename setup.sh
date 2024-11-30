#!/bin/bash

MODEL_URL="https://alphacephei.com/vosk/models/vosk-model-small-ru-0.22.zip"
MODEL_ZIP="vosk-model-small-ru-0.22.zip"
MODEL_DIR="vosk-model-small-ru-0.22"
VENV_DIR=".venv"
REQUIREMENTS_FILE="requirements.txt"

echo "Starting download of Vosk model..."

curl -o "$MODEL_ZIP" "$MODEL_URL"

if [ $? -ne 0 ]; then
    echo "Error: Failed to download the model from $MODEL_URL"
    exit 1
fi

echo "Download complete. Unpacking the model..."

unzip -o "$MODEL_ZIP"

if [ $? -ne 0 ]; then
    echo "Error: Failed to unpack the zip file."
    exit 1
fi

if [ -d "$MODEL_DIR" ]; then
    echo "Model unpacked successfully in the current folder: $MODEL_DIR"
else
    echo "Error: Model directory not found after unpacking."
    exit 1
fi

rm -f "$MODEL_ZIP"

echo "Setting up the Python virtual environment in $VENV_DIR..."
python3 -m venv "$VENV_DIR"

if [ $? -ne 0 ]; then
    echo "Error: Failed to create virtual environment."
    exit 1
fi

echo "Activating the virtual environment..."
source "$VENV_DIR/bin/activate"

if [ $? -ne 0 ]; then
    echo "Error: Failed to activate the virtual environment."
    exit 1
fi

if [ -f "$REQUIREMENTS_FILE" ]; then
    echo "Installing dependencies from $REQUIREMENTS_FILE..."
    pip install -r "$REQUIREMENTS_FILE"

    if [ $? -ne 0 ]; then
        echo "Error: Failed to install dependencies."
        deactivate
        exit 1
    fi
else
    echo "Warning: $REQUIREMENTS_FILE not found. Skipping dependency installation."
fi

echo "Launching flask app..."
gunicorn -w 4 -b 0.0.0.0:5000 recognizer:app

if [ $? -ne 0 ]; then
    echo "Error: Flask app failed to start."
    deactivate
    exit 1
fi