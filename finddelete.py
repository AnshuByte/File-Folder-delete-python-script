import os
import shutil

def find_files(file_names, search_paths):
    found_files = []
    for file_name in file_names:
        for path in search_paths:
            for root, dirs, files in os.walk(path):
                if file_name in files:
                    file_path = os.path.join(root, file_name)
                    found_files.append(file_path)
    return found_files

def find_folders(folder_name, search_paths):
    found_folders = []
    for path in search_paths:
        for root, dirs, files in os.walk(path):
            for dir_name in dirs:
                if dir_name == folder_name:
                    folder_path = os.path.join(root, dir_name)
                    found_folders.append(folder_path)
    return found_folders

def delete_files(file_paths):
    for file_path in file_paths:
        os.remove(file_path)
        print(f"Deleted {file_path}")

def delete_folders(folder_paths):
    for folder_path in folder_paths:
        shutil.rmtree(folder_path)
        print(f"Deleted folder {folder_path}")

if __name__ == "__main__":
    desktop_path = os.path.join(os.path.expanduser('~'), 'Desktop')
    downloads_path = os.path.join(os.path.expanduser('~'), 'Downloads')

    search_paths = [desktop_path, downloads_path]
    
    # Get file names from user
    file_names = input("Enter the names of the files to search for (comma separated, with extension): ").strip().split(',')
    file_names = [name.strip() for name in file_names]

    # Find files
    found_files = find_files(file_names, search_paths)
    
    if found_files:
        print("Found the following files:")
        for file_path in found_files:
            print(file_path)
        
        user_input = input("Do you want to delete all these files? (yes/no): ").strip().lower()
        if user_input == 'yes':
            delete_files(found_files)
        else:
            print("No files were deleted.")
    else:
        print("No files found matching the given names.")
    
    # Get folder name from user
    folder_name = input("Enter the name of the folder to search for: ").strip()

    # Find folders
    found_folders = find_folders(folder_name, search_paths)
    
    if found_folders:
        print("Found the following folders:")
        for folder_path in found_folders:
            print(folder_path)
        
        user_input = input("Do you want to delete all these folders? (yes/no): ").strip().lower()
        if user_input == 'yes':
            delete_folders(found_folders)
        else:
            print("No folders were deleted.")
    else:
        print(f"No folders named '{folder_name}' found in the specified directories.")
