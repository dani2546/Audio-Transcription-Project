
import os
import json
import whisper

# Load Whisper model
model = whisper.load_model("base")

def transcribe_with_timestamps(file_path):

    # Check whether the audio file exists
    if not os.path.isfile(file_path):
        print("Error: Audio file not found.")
        return None

    # Check audio format
    if not file_path.lower().endswith((".mp3", ".wav")):
        print("Error: Only MP3 and WAV files are supported.")
        return None

    try:
        print("Transcribing audio...")

        # Convert audio into text with timestamps
        result = model.transcribe(file_path, fp16=False)

        segments = []

        for segment in result["segments"]:

            data = {
                "start": round(segment["start"], 2),
                "end": round(segment["end"], 2),
                "text": segment["text"].strip()
            }

            segments.append(data)

            print(
                f"[{data['start']}s - {data['end']}s] "
                f"{data['text']}"
            )

        # Save transcription with timestamps
        output_file = os.path.splitext(file_path)[0] + ".json"

        with open(output_file, "w", encoding="utf-8") as file:
            json.dump(segments, file, indent=4, ensure_ascii=False)

        print("\nSaved at:", output_file)

        return segments

    except Exception as e:
        print("Error:", e)
        return None


if __name__ == "__main__":

    audio_path = input("Enter audio file path: ").strip().strip('"')

    transcribe_with_timestamps(audio_path)
