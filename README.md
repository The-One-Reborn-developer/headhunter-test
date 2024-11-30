# VOSK recognition app.

Flask app for VOSK speech recognition.

## Features

- Speech recognition from a local audio file.

## Dependencies

- [Flask](https://flask.palletsprojects.com/)
- [gunicorn](https://pypi.org/project/gunicorn/)
- [vosk](https://pypi.org/project/vosk/)
- [pydub](https://pypi.org/project/pydub/)

## Installation

Run the setup script:

```bash
source setup.sh
```

## Usage

Use the curl command to send a POST request to the app:

```bash
curl -X POST http://localhost:5000/ -H "Content-Type: application/json" -d '{"file_path": "path/to/audio/file.mp3"}'
```
