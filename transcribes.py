
import whisper
import os

# Folder containing audio files
folder_path = r"C:\Users\user\Downloads\songs"

# Load the speech recognition model
model = whisper.load_model("base")

# Supported audio formats
audio_formats = (".mp3", ".wav", ".m4a", ".flac")

# Check whether the folder exists
if not os.path.exists(folder_path):
    print("Folder not found!")
else:
    for file in os.listdir(folder_path):
        if file.lower().endswith(audio_formats):
            audio_path = os.path.join(folder_path, file)

            print("Transcribing:", file)

            try:
                # Convert speech into text
                result = model.transcribe(
                    audio_path,
                    fp16=False
                )

                text = result["text"]

                print("Transcription:")
                print(text)

                # Save transcription in a text file
                output_path = os.path.join(
                    folder_path,
                    os.path.splitext(file)[0] + ".txt"
                )

                with open(output_path, "w", encoding="utf-8") as f:
                    f.write(text)

                print("Saved:", output_path)

            except Exception as e:
                print("Error:", e)

    print("Process finished!")
