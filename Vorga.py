
import os
import shutil

def upload_audio():
    # Your audio folder path
    folder_path = r"C:\Users\user\Downloads\songs"

    # Folder to save uploaded files
    upload_folder = r"C:\Users\user\Downloads\uploaded_audio"

    # Check folder
    if not os.path.isdir(folder_path):
        print("Folder not found!")
        return

    # Find MP3 and WAV files
    audio_files = [
        file for file in os.listdir(folder_path)
        if file.lower().endswith((".mp3", ".wav"))
        and os.path.isfile(os.path.join(folder_path, file))
    ]

    if not audio_files:
        print("No audio files found!")
        return

    print("\nAvailable Audio Files:")

    for i, file in enumerate(audio_files, 1):
        print(f"{i}. {file}")

    # Select file
    try:
        choice = int(input("\nEnter file number: "))

        if choice < 1 or choice > len(audio_files):
            print("Invalid file number!")
            return

        file_name = audio_files[choice - 1]
        source = os.path.join(folder_path, file_name)

        # Create upload folder
        os.makedirs(upload_folder, exist_ok=True)

        destination = os.path.join(upload_folder, file_name)

        # Copy audio file
        shutil.copy2(source, destination)

        print("\nAudio file uploaded successfully!")
        print("File Name:", file_name)
        print("Saved At:", destination)

    except ValueError:
        print("Please enter a valid number!")

    except OSError as error:
        print("Error:", error)


# Start program
if __name__ == "__main__":
    upload_audio()
