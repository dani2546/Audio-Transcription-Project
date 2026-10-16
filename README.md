# Audio Transcription Project

This project has three simple Python scripts. They let me select an audio file, turn speech into text, and get text with timestamps.

## What each script does

| Question | File | What it does |
| --- | --- | --- |
| 1. Accept an audio file (WAV or MP3) | `Vorga.py` | Shows MP3/WAV files in a local folder, lets me choose one, and copies it to another folder. |
| 2. Transcribe spoken language into text | `transcribes.py` | Reads audio, converts speech to text using Whisper, prints the text, and saves a TXT file. |
| 3. Return transcription with timestamps per segment | `transcribe_timestamps.py` | Converts audio to text, shows the start and end time of each segment, and saves TXT and JSON files. |

## My approach and design decisions

I kept the project in three scripts because each question asks for a different task. This makes the code easier to read, test, and explain.

I used Python because it is simple to work with files. For speech recognition, I chose OpenAI Whisper's `base` model because it is a reasonable starting point for a small project. I set `fp16=False` so the scripts can run on a computer without a supported GPU.

For the first task, I let the user choose a file by number. I copy the file instead of moving it, so the original stays safe. For the second task, I save the text as a TXT file because it is easy to open. For the third task, I save both TXT and JSON. TXT is easy to read, while JSON keeps the exact start time, end time, and text of each segment.

I also added basic checks and error messages so the program can report a missing folder or a transcription problem.

## How I answer the three questions

### 1. How does the script accept WAV or MP3 files?
The first script checks a folder for MP3 and WAV files. It displays the available files, asks the user to enter a number, and copies the selected file to an upload folder. This is a local file-copy process, not a website upload.

### 2. How does the script convert speech into text?
The second script loads the Whisper model, checks the audio folder, and reads supported audio files. Whisper listens to the audio and returns the spoken words as text. The script prints the result and saves it in a TXT file.

### 3. How does the script return timestamps?
The third script uses Whisper's segments. Each segment has a start time, an end time, and spoken text. The script prints these details and saves them in TXT and JSON files. The displayed TXT times use minutes and seconds; JSON keeps the numeric times in seconds.

## Other design questions

These are ideas for improving the project later. **They are not all implemented in the three scripts.**

### How do you handle different audio formats?
The transcription scripts accept MP3, WAV, M4A, and FLAC file names. Whisper uses FFmpeg to read the audio. The file-selection script currently accepts only MP3 and WAV. If I want more formats in that script, I can add them to its allowed file list.

### How do you deal with long audio files?
At the moment, Whisper processes each audio file when the script reaches it. For very long files, I would split the audio into smaller parts, process them one by one, and join the results. I would adjust the timestamps so they still match the original recording.

### How would you handle concurrent uploads?
The current scripts run locally, one file at a time. For many users, I would build a web service that accepts uploads and puts them in a queue. Background workers could process different files without making users wait on the upload page.

### How would you store audio and transcripts?
Right now, audio stays in local folders and the scripts save TXT or JSON files next to the source audio. In a larger system, I would store uploaded audio in a separate storage folder or cloud storage. I would keep transcript files and basic details, such as file name and processing status, in organized storage or a database.

### How do you retry or recover failed transcriptions?
Right now, the scripts catch errors, print a message, and continue to the next file. They do not automatically retry. Later, I would save a failed job's status and retry it a limited number of times. I would also log the error so I can fix the problem.

### How would you expose this as an API?
The current project does not have an API. I would use Flask or FastAPI to add an endpoint such as `POST /transcribe`. A user could send an audio file and receive JSON containing the text and segment timestamps. For long jobs, the API could return a job ID and let the user check progress later.

## How to run in VS Code (Windows)

1. Install Python and FFmpeg. Check FFmpeg by running `ffmpeg -version` in the terminal.
2. Open this project folder in VS Code.
3. Install the Python dependency:

   ```powershell
   python -m pip install -r requirements.txt
   ```

4. Update `folder_path` in the three scripts to point to your audio folder. In `Vorga.py`, update `upload_folder` if needed. The original code uses `C:\Users\user\Downloads\songs`.
5. Run whichever script you need:

   ```powershell
   python Vorga.py
   python transcribes.py
   python transcribe_timestamps.py
   ```

The first Whisper run may download the model. Use the same Python interpreter for installation and running.

## Push this project to GitHub

Create an **empty** public repository named `Audio-Transcription-Project` at https://github.com/new. Do not initialize it with a README.

Open the project folder in VS Code, then run:

```powershell
git init
git branch -M main
git add .
git commit -m "Add scripts and design decisions README"
git remote add origin https://github.com/dani2546/Audio-Transcription-Project.git
git push -u origin main
```

If you already connected the `origin` remote, skip the `git remote add origin` command. If you already pushed the project, just run `git add README.md`, `git commit -m "Explain design decisions"`, and `git push`.

**Before publishing:** Do not include private recordings, transcripts, passwords, or large model files. The original Python scripts are kept unchanged.
