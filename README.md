Audio Transcription Pipeline
A simple Python project that accepts an MP3 or WAV audio file, converts speech into text using OpenAI Whisper, and returns timestamps for each spoken segment.

The project is divided into three scripts so each step can be run and tested separately.
Features
- Accepts MP3 and WAV audio files
- Checks whether the selected file exists and has a supported extension
- Copies the original audio into an uploads folder
- Converts speech into text using the open-source Whisper model
- Saves the transcription as a .txt file
- Returns segment-level start times, end times, and spoken text
- Saves timestamped results as a .json file
- Handles common errors such as missing files and unsupported extensions
Project Structure
audio-transcription-pipeline/
├── audio_upload.py       # Part 1: Accept and copy audio files
├── transcribes.py        # Part 2: Convert speech into text
├── timestamps.py         # Part 3: Generate timestamped segments
├── uploads/              # Created automatically by audio_upload.py
└── README.md
Requirements
- Python
- OpenAI Whisper
- FFmpeg installed and available in your system PATH
- Internet access the first time Whisper downloads its model
Install Whisper in the VS Code terminal:
python -m pip install -U openai-whisper
Note: FFmpeg must be installed separately. Check it using:
ffmpeg -version
How to Run
Open the project folder in VS Code and run the scripts in order.
Part 1: Accept an audio file
python audio_upload.py
When prompted, enter the full path to an MP3 or WAV file, for example:
C:\Users\user\Downloads\songs\Chan.mp3
The script checks the file and copies it into the uploads folder. The original file stays unchanged. A file with the same name in the uploads folder may be overwritten.
Part 2: Transcribe speech into text
python transcribes.py
Enter the path to the audio file, such as:
uploads\Chan.mp3
The script uses Whisper's base model to recognize speech, displays the transcription, and saves a text file next to the audio file (for example, uploads\Chan.txt).
Part 3: Generate timestamps for each segment
python timestamps.py
Enter the audio file path again:
uploads\Chan.mp3
The script prints each segment with its start and end time and saves the result as JSON (for example, uploads\Chan.json).
Example Output
Example terminal output (illustrative; actual text and timestamps depend on the audio):
[0.0s - 2.5s] Hello everyone.
[2.5s - 5.8s] Welcome to today's meeting.
[5.8s - 9.2s] We will discuss our project.
Example JSON:
[
  {
    "start": 0.0,
    "end": 2.5,
    "text": "Hello everyone."
  },
  {
    "start": 2.5,
    "end": 5.8,
    "text": "Welcome to today's meeting."
  },
  {
    "start": 5.8,
    "end": 9.2,
    "text": "We will discuss our project."
  }
]
How It Works
1. Audio input: audio_upload.py checks the path and extension, then copies the file to uploads/.
2. Speech-to-text: transcribes.py loads Whisper and converts the audio into plain text.
3. Timestamped transcription: timestamps.py runs Whisper and saves each detected segment with its start time, end time, and text.
The second and third scripts run transcription independently; the third script does not read the text file created by the second script.
Engineering Decisions
- Python: Easy to read, test, and maintain.
- Whisper base model: A practical balance between speed and transcription quality for a small project; no model training is needed.
- Copy instead of move: Keeps the original audio file safe.
- Text output: Easy for people to read.
- JSON output: Easy for other programs and APIs to process.
- Segment timestamps: Useful for finding when a sentence or phrase was spoken.
- fp16=False: Allows Whisper to run on a CPU without the FP16 warning.
Limitations and Future Improvements
- File validation currently checks the filename extension, not the actual audio content.
- Large audio files may take longer to process, especially on a CPU.
- Segment timestamps are approximate and are not word-by-word timestamps.
- The upload script may overwrite an existing file with the same name.
- For production use, add file-size limits, unique filenames, stronger file validation, logging, and background processing for concurrent uploads.
- The three scripts could be combined into one service or exposed through an API in a future version.
Summary
This project demonstrates a simple, modular audio transcription pipeline using Python and Whisper. It accepts an audio file, converts spoken language into text, and produces timestamped JSON that can be used by downstream applications.
