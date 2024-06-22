import os
import shutil

# Directory where downloaded files are stored
download_dir = r'C:/Users/KIIT/Desktop/my Den/Books'

# Create a folder named "organized_files"
organized_dir = os.path.join(download_dir, 'organized_files')
os.makedirs(organized_dir, exist_ok=True)

# Create subfolders for different file types
folders = {
    'documents': ['pdf', 'txt', 'docx', 'epub'],
    'videos': ['mp4', 'mkv'],
    'photos': ['jpeg', 'jpg', 'png', 'gif'],
    'Maya': ['mb'],
    'Figma': ['fig'],
    'audios': ['m4b'],
}

for folder in folders.keys():
    main_folder_path = os.path.join(organized_dir, folder)
    os.makedirs(main_folder_path, exist_ok=True)

# List files in the download directory
files = os.listdir(download_dir)

for file in files:
    # Get the full path of the file
    file_path = os.path.join(download_dir, file)
    
    # Check if it's a directory, if so, skip
    if os.path.isdir(file_path):
        print(f"Ignored {file}: Directory")
        continue
    
    # Get the file extension
    file_ext = file.split('.')[-1].lower()
    
    # Find the destination folder for the file
    dest_folder = None
    for folder, exts in folders.items():
        if file_ext in exts:
            dest_folder = folder
            break
    
    # Move files to respective folders
    if dest_folder:
        dest_folder_path = os.path.join(organized_dir, dest_folder, file_ext)
        os.makedirs(dest_folder_path, exist_ok=True)
        src_path = os.path.join(download_dir, file)
        dest_path = os.path.join(dest_folder_path, file)
        shutil.move(src_path, dest_path)
        print(f"Moved {file} to {dest_folder}/{file_ext}/{file} folder.")
    else:
        print(f"Ignored {file}: Unknown file type.")

print("Organizing files completed.")
