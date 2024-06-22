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

def find_folders(folder_names, search_paths):
    found_folders = []
    for folder_name in folder_names:
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
    
    # Default file names to delete
    file_names = ["Platforms.pdf", "Courses.pdf", "Free.docx", 
                  "Introduction.txt", "Gift.pdf", "money.com - VIP.txt", 
                  ]

    # Default folder names to delete
    folder_names = ["00-Join For Free Courses", "00- Join to Learn"]

    while True:
        # Find files and folders
        found_files = find_files(file_names, search_paths)
        found_folders = find_folders(folder_names, search_paths)
        
        if found_files or found_folders:
            if found_files:
                print("Found the following files:")
                for file_path in found_files:
                    print(file_path)
            
            if found_folders:
                print("Found the following folders:")
                for folder_path in found_folders:
                    print(folder_path)
            
            # Ask for confirmation before deleting files and folders
            delete_confirmation = input("Do you want to delete these files and folders? (yes/no): ").strip().lower()
            if delete_confirmation == 'yes':
                if found_files:
                    delete_files(found_files)
                if found_folders:
                    delete_folders(found_folders)
            else:
                print("Files and folders were not deleted.")
        
        else:
            print("No files or folders found matching the given names.")
        
        # Ask if there are any more files or folders to delete
        more_deletion = input("Do you want to delete any more files or folders? (yes/no): ").strip().lower()
        if more_deletion == 'yes':
            new_file_names = input("Enter the names of files to delete, separated by commas: ").strip().split(',')
            new_folder_names = input("Enter the names of folders to delete, separated by commas: ").strip().split(',')
            
            # Strip any extra whitespace from the names
            new_file_names = [name.strip() for name in new_file_names]
            new_folder_names = [name.strip() for name in new_folder_names]
            
            # Find and delete the new files and folders
            new_found_files = find_files(new_file_names, search_paths)
            new_found_folders = find_folders(new_folder_names, search_paths)
            
            if new_found_files or new_found_folders:
                if new_found_files:
                    print("Found the following files:")
                    for file_path in new_found_files:
                        print(file_path)
                
                if new_found_folders:
                    print("Found the following folders:")
                    for folder_path in new_found_folders:
                        print(folder_path)
                
                # Ask for confirmation before deleting new files and folders
                delete_new_confirmation = input("Do you want to delete these files and folders? (yes/no): ").strip().lower()
                if delete_new_confirmation == 'yes':
                    if new_found_files:
                        delete_files(new_found_files)
                    if new_found_folders:
                        delete_folders(new_found_folders)
                else:
                    print("Files and folders were not deleted.")
            else:
                print("No additional files or folders found matching the given names.")
        else:
            print("No more deletions requested.")
            break
