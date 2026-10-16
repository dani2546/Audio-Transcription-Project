
import whisper
import os
import json

# Folder containing audio files
folder_path = r"C:\Users\user\Downloads\songs"

# Load Whisper model
model = whisper.load_model("base")

# Supported audio formats
audio_formats = (".mp3", ".wav", ".m4a", ".flac")

# Convert seconds into timestamp format
def format_time(seconds):
    minutes = int(seconds // 60)
    remaining_seconds = int(seconds % 60)
    return f"{minutes:02d}:{remaining_seconds:02d}"

# Check folder
if not os.path.exists(folder_path):
    print("Folder not found!")

else:
    for file in os.listdir(folder_path):

        if file.lower().endswith(audio_formats):

            audio_path = os.path.join(folder_path, file)

            print("\nTranscribing:", file)

            try:
                # Convert audio into text
                result = model.transcribe(
                    audio_path,
                    fp16=False
                )

                segments = []

                # Get text with timestamps
                for segment in result["segments"]:

                    start = format_time(segment["start"])
                    end = format_time(segment["end"])
                    text = segment["text"].strip()

                    print(f"[{start} - {end}] {text}")

                    segments.append({
                        "start": segment["start"],
                        "end": segment["end"],
                        "text": text
                    })

                # Save transcription as TXT
                txt_path = os.path.splitext(audio_path)[0] + ".txt"

                with open(txt_path, "w", encoding="utf-8") as f:
                    for segment in segments:
                        start = format_time(segment["start"])
                        end = format_time(segment["end"])
                        f.write(
                            f"[{start} - {end}] {segment['text']}\n"
                        )

                # Save transcription as JSON
                json_path = os.path.splitext(audio_path)[0] + ".json"

                with open(json_path, "w", encoding="utf-8") as f:
                    json.dump(segments, f, indent=4, ensure_ascii=False)

                print("Transcription saved successfully!")

            except Exception as e:
                print("Error:", e)

    print("\nProcess finished!")

