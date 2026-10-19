
import os
import shutil

# Folder where audio files will be saved
UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# Supported audio formats
ALLOWED_FORMATS = [".mp3", ".wav"]

def upload_audio(file_path):
    # Check if file exists
    if not os.path.isfile(file_path):
        print("Error: File not found.")
        return None

    # Check file format
    file_name = os.path.basename(file_path)
    extension = os.path.splitext(file_name)[1].lower()

    if extension not in ALLOWED_FORMATS:
        print("Error: Only MP3 and WAV files are supported.")
        return None

    # Copy audio file to uploads folder
    destination = os.path.join(UPLOAD_FOLDER, file_name)
    shutil.copy2(file_path, destination)

    print("Audio uploaded successfully!")
    print("Saved at:", destination)

    return destination


# Main program
if __name__ == "__main__":
    audio_path = input("Enter audio file path: ").strip().strip('"')
    upload_audio(audio_path)
