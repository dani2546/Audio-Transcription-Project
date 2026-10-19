
import os
import whisper

# Load speech-to-text model
model = whisper.load_model("base")

def transcribe_audio(file_path):

    # Check whether the file exists
    if not os.path.isfile(file_path):
        print("Error: Audio file not found.")
        return

    # Check audio format
    if not file_path.lower().endswith((".mp3", ".wav")):
        print("Error: Only MP3 and WAV files are supported.")
        return

    try:
        print("Transcribing audio...")

        # Convert speech into text
        result = model.transcribe(file_path, fp16=False)

        transcription = result["text"].strip()

        print("\nTranscription:")
        print(transcription)

        # Save transcription to a text file
        output_file = os.path.splitext(file_path)[0] + ".txt"

        with open(output_file, "w", encoding="utf-8") as file:
            file.write(transcription)

        print("\nTranscription saved at:", output_file)

        return transcription

    except Exception as e:
        print("Transcription failed:", e)


if __name__ == "__main__":
    audio_path = input("Enter audio file path: ").strip().strip('"')
    transcribe_audio(audio_path)
