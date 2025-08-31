import os
import shutil

# 📂 Folder you want to organize
folder_path = "Day2/TestFolder"   # change this to your test folder

# File type categories
file_types = {
    "Images": [".jpg", ".jpeg", ".png", ".gif"],
    "Documents": [".pdf", ".docx", ".txt", ".xlsx"],
    "Music": [".mp3", ".wav"],
    "Videos": [".mp4", ".mov", ".avi"],
    "Archives": [".zip", ".rar", ".tar", ".gz"]
}

# Create category folders if not present
for folder in file_types.keys():
    os.makedirs(os.path.join(folder_path, folder), exist_ok=True)

# Go through each file
for filename in os.listdir(folder_path):
    file_path = os.path.join(folder_path, filename)

    if os.path.isfile(file_path):  # skip folders
        moved = False
        for folder, extensions in file_types.items():
            if any(filename.lower().endswith(ext) for ext in extensions):
                shutil.move(file_path, os.path.join(folder_path, folder, filename))
                print(f"Moved: {filename} → {folder}/")
                moved = True
                break

        if not moved:
            # If file type doesn’t match, put it in "Others"
            other_folder = os.path.join(folder_path, "Others")
            os.makedirs(other_folder, exist_ok=True)
            shutil.move(file_path, os.path.join(other_folder, filename))
            print(f"Moved: {filename} → Others/")
